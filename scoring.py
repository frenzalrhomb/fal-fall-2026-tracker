"""Fall 2026 rule arithmetic. None represents an unobserved scoring input."""
EVEN = {2, 4, 6, 8, 10, 12}
SCORE = {3, 7, 10, 13}
DROPS = {4, 8, 11, 13}
FAVORITES = {5, 9, 12, 13}
DISCUSSION = EVEN | {13}


def weekly_components(week, metrics, *, aired, bonus_mode):
    """episode_participants = sum of distinct users PER eligible episode thread.
    Caller must resolve FAL bonus semantics. None stays None on scoring weeks.
    These are base anime points only, excluding team actions.
    """
    if week not in range(1,14):
        raise ValueError("Week must be 1..13")
    if bonus_mode not in ("additive","replacement","fal_2026"):
        raise ValueError("Explicit bonus_mode required")
    def rate(base, bonus):
        return base+bonus if bonus_mode=="additive" else bonus
    def mul(key, weight):
        value=metrics.get(key)
        return None if value is None else value*weight
    wc = (metrics["watching"]+metrics["completed"]) if all(metrics.get(k) is not None for k in ("watching","completed")) else None
    watching_weight=(.75 if bonus_mode=="fal_2026" else rate(.5,.25)) if week in EVEN else .5
    audience=0 if not aired else (None if wc is None else wc*watching_weight)
    def final_weight(base, bonus):
        return bonus if bonus_mode=="fal_2026" else rate(base,bonus)
    discussion_weight=final_weight(75,150) if week==13 else 75
    score_weight=final_weight(17500,35000) if week==13 else 17500
    drop_weight=final_weight(-4,-8) if week==13 else -4
    favorite_weight=final_weight(15,30) if week==13 else 15
    score=metrics.get("score")
    result={"audience":audience,
            "discussions":mul("episode_participants",discussion_weight) if week in DISCUSSION else 0,
            "score":(None if score is None else (score-6)*score_weight) if week in SCORE else 0,
            "dropped":mul("dropped",drop_weight) if week in DROPS else 0,
            "favorites":mul("favorites",favorite_weight) if week in FAVORITES else 0}
    result["total"]=sum(result.values()) if all(v is not None for v in result.values()) else None
    result["known_subtotal"]=sum(result[k] for k in ("audience","discussions","score","dropped","favorites") if result[k] is not None)
    result["missing"]=[k for k in ("audience","discussions","score","dropped","favorites") if result[k] is None]
    return result
