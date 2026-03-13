
IMPLEMENTATION GUIDE

Step 1 — Dataset Design
We define dataset fields:
image_id, file_name, label, scenario, lighting, blur_score, split

Step 2 — Data Collection
Images are synthetically generated with labels representing robot tasks.

Step 3 — Metadata Generation
Each image gets metadata describing capture conditions and training label.

Step 4 — SQL Layer
Metadata is stored in SQLite so it can be queried using SQL.

Step 5 — Validation
We check:
missing labels
blurry images
dataset size

Step 6 — Dashboarding
Charts are generated showing label distribution, scenario distribution, and train/val/test split.

Step 7 — Stakeholder Reporting
The dashboard HTML acts as a Tableau-style artifact summarizing dataset health.
