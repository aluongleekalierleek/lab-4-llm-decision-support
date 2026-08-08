SUMMARY_PROMPT = """Summarize the loan letter. Include name, loan amount, purpose, repayment plan, collateral. Do not invent details."""

EXTRACT_PROMPT = """Extract loan details as JSON with keys: applicant_name, amount_ghs, purpose, monthly_profit_ghs, has_collateral_or_guarantor, repayment_months. Use null if missing. Do not guess."""

BRIEF_PROMPT = """Make a decision-support brief. Show strengths, risks, missing info, and suggest next step (like interview or request documents). Do not say approve or reject. Final decision is for humans."""
