from django.db import migrations

# If you want to treat the existing times as "today at that time" in UTC:
TZ = "UTC"  # or "Asia/Kolkata" if you want to treat the old time as local IST

SQL_UP = f"""
ALTER TABLE users_student
ALTER COLUMN start_time
TYPE timestamptz
USING ((CURRENT_DATE::timestamp + start_time) AT TIME ZONE '{TZ}');

ALTER TABLE users_student
ALTER COLUMN end_time
TYPE timestamptz
USING ((CURRENT_DATE::timestamp + end_time) AT TIME ZONE '{TZ}');
"""

SQL_DOWN = """
ALTER TABLE users_student
ALTER COLUMN start_time TYPE time USING (start_time::time);

ALTER TABLE users_student
ALTER COLUMN end_time TYPE time USING (end_time::time);
"""

class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_remove_student_log_student_logs"),  # <-- keep the exact last good migration name from your repo
    ]

    operations = [
        migrations.RunSQL(SQL_UP, SQL_DOWN),
    ]


