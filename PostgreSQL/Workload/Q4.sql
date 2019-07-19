set search_path to td;
select matchft.round_id,  rounddt.round ,avg(matchft.w_bpsaved_pctg) as avg_bpsaved_pctg
from matchft , rounddt
where matchft.round_id = rounddt.round_id
group by matchft.round_id , rounddt.round
order by round_id