-- X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, visit_date, people

-- Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

-- For example, the table stadium:
-- +------+------------+-----------+
-- | id   | visit_date | people    |
-- +------+------------+-----------+
-- | 1    | 2017-01-01 | 10        |
-- | 2    | 2017-01-02 | 109       |
-- | 3    | 2017-01-03 | 150       |
-- | 4    | 2017-01-04 | 99        |
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- For the sample data above, the output is:

-- +------+------------+-----------+
-- | id   | visit_date | people    |
-- +------+------------+-----------+
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- Note:
-- Each day only have one row record, and the dates are increasing with id increasing.

create or replace view rows_over_hundrand AS 
SELECT 
    id
    , visit_date
    , people
FROM 
stadium
WHERE people >= 100;

create or replace view consecutive_days as
select 
r1.id as hid, r2.id as tid
rows_over_hundrand r1 
join 
rows_over_hundrand r2 
on r1.id-r2.id = 1 

create or replace view consecutive_days_2 as 
select
r1.hid as hid, r2.tid as tid 
from 
consecutive_days r1 
join 
consecutive_days r2 
on r1.hid-r2.hid = 1;

select s.* from 
(
select
hid 
from 
consecutive_days_2  r1
join 
consecutive_days_2 r2 
on r1.hid-h2.hid = 2 
) a 
join
stadium s 
on a.hid=s.id


