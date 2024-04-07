CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age INT
);

CREATE TABLE logs (
    log_id SERIAL PRIMARY KEY,
    user_id INT,
    user_action VARCHAR(50),
    user_time TIMESTAMP DEFAULT NOW()
);

CREATE PROCEDURE new_user(
    first_name_param VARCHAR(100), 
    last_name_param VARCHAR(100),
    age_param INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO users (first_name, last_name, age)
    VALUES (first_name_param, last_name_param, age_param);
END;
$$;

CREATE PROCEDURE new_log(
    user_id_param INT, 
    user_action_param VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO logs (user_id, user_action)
    VALUES (user_id_param, user_action_param);
END;
$$;

CREATE FUNCTION get_full_name(user_id_param INT)
RETURNS VARCHAR(200)
AS $$
DECLARE
    full_name VARCHAR(200);
BEGIN
    SELECT CONCAT(fist_name, ' ', last_name) 
    INTO full_name
    FROM users
    WHERE user_id = user_id_param;
    RETURN full_name;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION log_trigger_function()
RETURNS TRIGGER
AS $$
BEGIN
    CALL new_log(NEW.user_id, TG_OP);
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER user_action_trigger
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW 
EXECUTE FUNCTION log_trigger_function();