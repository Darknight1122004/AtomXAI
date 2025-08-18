from django.db import migrations

TZ = "UTC"  # or "Asia/Kolkata"

SQL_UP = f"""
ALTER TABLE users_student
  ALTER COLUMN start_time TYPE timestamptz
  USING ((CURRENT_DATE::timestamp + start_time) AT TIME ZONE '{TZ}');

ALTER TABLE users_student
  ALTER COLUMN end_time TYPE timestamptz
  USING ((CURRENT_DATE::timestamp + end_time) AT TIME ZONE '{TZ}');
"""

SQL_DOWN = """
ALTER TABLE users_student
  ALTER COLUMN start_time TYPE time USING (start_time::time);
ALTER TABLE users_student
  ALTER COLUMN end_time   TYPE time USING (end_time::time);
"""

class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_remove_student_log_student_logs"),  # <-- EXACT 0010 file stem
    ]
    operations = [
        migrations.RunSQL(SQL_UP, SQL_DOWN),
    ]
