set search_path to td;
CREATE VIEW finals AS
    SELECT *
    FROM matchft
    WHERE round_id = 7;