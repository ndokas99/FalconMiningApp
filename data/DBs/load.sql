create table explosives(expname text, amount integer, 'favourable conditions' text);
create table "geology and survey"(section integer, 'section ore grade' integer, 'geometrical position' text, 'average ucs of exposed ore' integer, 'rmr of exposed ore' integer, 'Average dip angle of joints' integer, 'Average dip angle of strike' integer);
create table machinery(machname text, type text, 'efficiency update' text, 'drill-hole diameter' text, 'working rate' text, 'maximum stable speed' integer, capacity integer, 'fuel type' text, 'favourable conditions' text);

insert into explosives values ("ANFO", 10, "most rock types");
insert into explosives values ("TNT", 300, "hard rocks");
insert into explosives values ("BOOSTERS", 50, "very hard rocks");
insert into explosives values ("EMULSIONS", 800, "watery conditions");

insert into "geology and survey" values (1, "high grade", "1.5m West;2.0m North,…", 30, 50, 10, 40);
insert into "geology and survey" values (2, "medium grade", "0.8m East; 0.5m South", 60, 80, 25, 32);

insert into machinery values ("AD60 dump truck","hauling truck",91,"","high bucket-fill",85,500,"diesel","");
insert into machinery values ("Jack hammer","hand held drilling",97,"60-110mm","0.2m/h",0,0,"water","fairly soft rock");
insert into machinery values ("Joy DR-2SB","drilling",77,"85-120mm","1.0m/h",0,0,"diesel and electricity","fairly hard rock");
insert into machinery values ("DC-726B drill rig","drilling",80,"90-130mm","2.5m/h",0,0,"diesel","very hard rock ore");
insert into machinery values ("LHD","hauling",0,"","small bucket-fill time",80,150,"diesel","");
