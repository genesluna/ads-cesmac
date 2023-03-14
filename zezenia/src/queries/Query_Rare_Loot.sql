SELECT monsters.*
FROM monsters
JOIN monster_rare_loot ON monsters.id = monster_rare_loot.monster_id
JOIN rare_loot ON monster_rare_loot.rare_loot_id = rare_loot.id
WHERE rare_loot.name = 'Golden Axe';
