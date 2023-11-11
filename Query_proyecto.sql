create table departamento
(
	id varchar(10),
	nombre varchar(30),
	primary key (id)
);

create table municipio
(
	id varchar(10),
	nombre varchar(30),
	id_dept varchar(10),
	primary key (id),
	foreign key (id_dept) references departamento(id)
);

create table colegio
(
	id varchar(12),
	nombre varchar(100),
	id_mun_loc varchar(10),
	primary key (id),
	foreign key (id_mun_loc) references municipio(id)
);

create table institucion
(
	codigo varchar(10),
	nombre varchar(50),
	caracter_academico varchar(40),
	origen varchar(40),
	id_mun_pres varchar(10),
	primary key (codigo),
	foreign key (id_mun_pres) references municipio(id)
);

create table estudiante
(
	id varchar(14),
	pais_residencia varchar(50),
	fecha_nacimiento date,
	tipo_documento varchar(5),
	nacionalidad varchar(50),
	genero varchar(1),
	beca varchar(2),
	credito varchar(2),
	id_mun_res varchar(10),
	id_colegio varchar(12),
	primary key (id),
	foreign key (id_mun_res) references municipio(id),
	foreign key (id_colegio) references colegio(id)
); 

create table estudia
(
	id_estu varchar(14),
	cod_insti varchar(10),
	nombre varchar(40),
	nivel varchar(30),
	metodo varchar(30),
	primary key (id_estu,cod_insti),
	foreign key (id_estu) references estudiante(id),
	foreign key (cod_insti) references institucion(codigo)
);

create table familia
(
	id_estu varchar(14),
	educacion_madre varchar(40),
	educacion_padre varchar(40),
	tiene_automovil varchar(2),
	tiene_internet varchar(2),
	tiene_lavadora varchar(2),
	tiene_computadora varchar(2),
	estrato varchar(11),
	primary key (id_estu),
	foreign key (id_estu) references estudiante(id)
);

create table prueba
(
	id_estu varchar(14),
	id_mun_desarrollo varchar(10),
	punt_razonamiento_cuantitativo numeric(3,0),
	punt_comunicacion_escrita numeric(3,0),
	punt_lectura_critica numeric(3,0),
	punt_ingles numeric(3,0),
	punt_competencias_ciudadanas numeric(3,0),
	desem_ingles varchar(2),
	desem_comunicacion_escrita numeric(1,0),
	primary key (id_estu),
	foreign key (id_estu) references estudiante(id),
	foreign key (id_mun_desarrollo) references municipio(id)
);

