def build_decision(answers, judges):
    votes = [j["selected"] for j in judges.values()]
    selected = max(set(votes), key=votes.count)

    vote_count = votes.count(selected)
    total_judges = len(votes)
    confidence_score = vote_count / total_judges

    citations = answers[selected]["citations"]
    risks = list(set(sum([j["risks"] for j in judges.values()], [])))

    return {
        "final_answer": answers[selected]["text"],
        "confidence": {
            "score": confidence_score,
            "method": (
                "unanimous_judge_agreement"
                if confidence_score == 1.0
                else "partial_judge_agreement"
            ),
            "votes": f"{vote_count}/{total_judges}"
        },
        "selected_agent": selected,
        "risks": risks,
        "citations": citations,
        "judge_votes": votes
    }
