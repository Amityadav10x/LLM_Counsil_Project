from agents.answer_agent import generate_answer
from agents.judge_agent import judge
from safety.input_gate import validate_input
from safety.output_gate import validate_output
from decision.decision_builder import build_decision
from audit.logger import log

# -----------------------------
# 1. User Prompt
# -----------------------------
PROMPT = "Explain the benefits of solar energy"

print("Validating input...")
validate_input(PROMPT)

# -----------------------------
# 2. Generate Answers (3 agents)
# -----------------------------
print("Running answer agents...")

from config import ANSWER_AGENTS

answers = {
    key: generate_answer(PROMPT, prompt)
    for key, prompt in ANSWER_AGENTS.items()
}


print("Answers generated")

# -----------------------------
# 3. Output Safety Check
# -----------------------------
all_risks = []
for key, ans in answers.items():
    risks = validate_output(ans["text"])
    all_risks.extend(risks)

# -----------------------------
# 4. Judge Comparison (2 judges)
# -----------------------------
print("Running judges...")

judges = {
    "judge_1": judge(PROMPT, answers, "judge_1"),
    "judge_2": judge(PROMPT, answers, "judge_2")
}

print("Judging completed")

# -----------------------------
# 5. Build Final Decision Object
# -----------------------------
decision = build_decision(answers, judges)

# Include safety risks if any
decision["risks"].extend(all_risks)
decision["risks"] = list(set(decision["risks"]))

# -----------------------------
# 6. Audit Log (Persistent)
# -----------------------------
log({
    "prompt": PROMPT,
    "answers": answers,
    "judges": judges,
    "decision": decision
})

# -----------------------------
# 7. Print Final Output
# -----------------------------
print("\nFINAL DECISION OBJECT:\n")
print(decision)
