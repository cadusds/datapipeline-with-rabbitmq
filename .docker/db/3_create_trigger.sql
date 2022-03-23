create trigger test_notify_changes
after insert or update or delete
on test
for each row
execute procedure notify_changes()