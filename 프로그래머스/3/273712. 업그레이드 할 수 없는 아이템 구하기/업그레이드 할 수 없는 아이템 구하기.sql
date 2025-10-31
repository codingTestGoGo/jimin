select a.item_id, a.item_name, a.rarity
from item_info a
where not exists(
    select 1
    from item_tree b
    where b.parent_item_id = a.item_id
)
order by a.item_id desc