create table icfes(
a1 varchar(1000),
a2 varchar(1000),
a3 varchar(1000),
a4 varchar(1000),
a5 varchar(1000),
a6 varchar(1000),
a7 varchar(1000),
a8 varchar(1000),
a9 varchar(1000),
a10 varchar(1000),
a12 varchar(1000),
a13 varchar(1000),
a14 varchar(1000),
a15 varchar(1000),
a16 varchar(1000),
a17 varchar(1000),
a18 varchar(1000),
a19 varchar(1000),
a20 varchar(1000),
a21 varchar(1000),
a22 varchar(1000),
a23 varchar(1000),
a24 varchar(1000),
a25 varchar(1000),
a26 varchar(1000),
a27 varchar(1000),
a28 varchar(1000),
a29 varchar(1000),
a30 varchar(1000),
a31 varchar(1000),
a32 varchar(1000),
a33 varchar(1000),
a34 varchar(1000),
a35 varchar(1000),
a36 varchar(1000),
a37 varchar(1000),
a38 varchar(1000),
a39 varchar(1000),
a40 varchar(1000),
a41 varchar(1000),
a42 varchar(1000),
a43 varchar(1000),
a44 varchar(1000),
a45 varchar(1000),
a46 varchar(1000),
a47 varchar(1000),
a48 varchar(1000),
a49 varchar(1000),
a50 varchar(1000),
a51 varchar(1000),
a52 varchar(1000),
a53 varchar(1000),
a54 varchar(1000),
a55 varchar(1000),
a56 varchar(1000),
a57 varchar(1000)
);

COPY icfes (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57)
FROM 'C:\Users\JoseDanielMejia\Downloads\icfes.csv'
DELIMITER ','
CSV HEADER;

insert into departamento select distinct a5, a6 from icfes;

insert into municipio select distinct a7,a8,a5 from icfes;

insert into estudiante select distinct a2,a4,cast(a40 as date),a3,a34,a36,a29,a30,a7,a9 from icfes;

insert into institucion select distinct a12,a13,a14,a50,a17 from icfes;

insert into estudia select distinct a2,a12,a15,a23,a24 from icfes;

insert into familia select distinct a2,a49,a43,a44,a48,a45,a47,a46 from icfes;

insert into prueba select distinct a2,cast(a51 as numeric(3,0)),cast(a52 as numeric(3,0)),cast(a55 as numeric(3,0)),cast(a56 as numeric(3,0)),cast(a57 as numeric(3,0)),a54,cast(a53 as numeric(1,0))
from icfes;

CREATE ROLE taylor with
LOGIN
NOSUPERUSER
NOCREATEDB
NOCREATEROLE
INHERIT
NOREPLICATION
CONNECTION LIMIT -1
PASSWORD '1234';
COMMENT ON ROLE taylor is 'Usuario para consultar en python';

grant select on estudiante, departamento, familia, prueba, municipio, institucion, estudia to taylor;
