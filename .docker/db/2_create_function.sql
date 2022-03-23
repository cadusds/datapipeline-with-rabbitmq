create or replace function notify_changes()
returns trigger as $$
begin
    perform pg_notify(
        'changes',
        json_build_object(
            'table',TG_TABLE_NAME,
            'operation',TG_OP,
            'record',row_to_json(NEW)
        )::text
    );

    return NEW;
end;
$$ language plpgsql;