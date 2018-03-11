CREATE TYPE IS_APPLICABLE AS ENUM(
	'Y',
	'N',
	'NYA'	
);

CREATE TYPE TRACK_CATEGORY AS ENUM(
	'SOL_TRACK',
	'SOL_TUNNEL',
	'OP_TRACK',
	'OP_TRACK_TUNNEL',
	'OP_TRACK_PLATFORM',
	'OP_SIDING',
	'OP_SIDING_TUNNEL'
);

CREATE TABLE IF NOT EXISTS MEMBER (
	MEM_id varchar PRIMARY KEY,
	MEM_version varchar
);

CREATE TABLE IF NOT EXISTS LINE (
	LIN_id varchar PRIMARY KEY,
	LIN_name varchar, 
	MEM_id varchar REFERENCES MEMBER
);

CREATE TABLE OP_TYPE (
	OTY_id varchar PRIMARY KEY,
	OTY_name varchar
);

CREATE TABLE IF NOT EXISTS OPERATIONAL_POINT (
	OPP_id varchar PRIMARY KEY,
	OPP_name varchar ,
	OPP_uniqueid varchar ,
	OPP_lon float8 ,
	OPP_lat float8 ,
	OPP_geom geometry(Point, 4326),
	OPP_taftapcode varchar ,
	OPP_date_start varchar, 
	OPP_date_end varchar,
	OTY_id varchar REFERENCES OP_TYPE,
	MEM_id varchar REFERENCES MEMBER
);


CREATE TABLE IF NOT EXISTS SECTION_OF_LINE (
	SOL_id varchar PRIMARY KEY,
	SOL_length float8 ,
	SOL_nature varchar,
	SOL_imcode int ,
	OPP_start varchar REFERENCES OPERATIONAL_POINT,
	OPP_end varchar  REFERENCES OPERATIONAL_POINT,
	MEM_id varchar  REFERENCES MEMBER,
	SOL_date_start varchar ,
	SOL_date_end varchar ,
	LIN_id varchar  REFERENCES LINE
);

CREATE TABLE IF NOT EXISTS OP_TRACK (
	OTR_id varchar PRIMARY KEY,
	OTR_name varchar ,
	OTR_imcode int,
	OTR_date_start varchar,
    OTR_date_end varchar,
	OPP_id varchar REFERENCES OPERATIONAL_POINT

);

CREATE TABLE IF NOT EXISTS OP_SIDING (
	OSI_id varchar PRIMARY KEY,
	OSI_name varchar ,
	OSI_imcode int,
	OSI_date_start varchar,
    OSI_date_end varchar,
	OPP_id varchar REFERENCES OPERATIONAL_POINT

);

CREATE TABLE IF NOT EXISTS SOL_TRACK (
	STR_id varchar PRIMARY KEY,
	STR_name varchar ,
	STR_direction  varchar,
	STR_date_start varchar,
	STR_date_end varchar,
	SOL_id varchar REFERENCES SECTION_OF_LINE 

);

CREATE TABLE RAILWAY_LOCATION (
	RAL_id varchar PRIMARY KEY,
	RAL_distance float8 ,
	RAL_natid varchar ,
	OPP_id varchar REFERENCES OPERATIONAL_POINT
	--,LIN_id varchar REFERENCES LINE
);

CREATE TABLE IF NOT EXISTS SOL_TUNNEL (
	STU_id varchar PRIMARY KEY,
	STU_name varchar ,
	STU_startlon float8 ,
	STU_startlat float8 ,
	STU_start_geom geometry(Point, 4326),
	STU_endlon float8 ,
	STU_endlat float8 ,
	STU_end_geom geometry(Point, 4326),
	STU_imcode int , 
	STU_date_start varchar,
	STU_date_end varchar,
	STR_id varchar REFERENCES SOL_TRACK

);

CREATE TABLE IF NOT EXISTS OP_TRACK_TUNNEL (
	OTU_id varchar PRIMARY KEY,
	OTU_name varchar ,
	OTU_imcode int, 
	OTU_date_start varchar,
	OTU_date_end varchar,
	OTR_id varchar REFERENCES OP_TRACK
);

CREATE TABLE IF NOT EXISTS OP_TRACK_PLATFORM (
	OPL_id varchar PRIMARY KEY ,
	OPL_name varchar ,
	OPL_imcode int,
	OPL_date_start varchar,
	OPL_date_end varchar,
	OTR_id varchar REFERENCES OP_TRACK

);

CREATE TABLE IF NOT EXISTS OP_SIDING_TUNNEL (
	OST_id varchar PRIMARY KEY,
	OST_name varchar ,
	OST_imcode int, 
	OST_date_start varchar,
	OST_date_end varchar,
	OSI_id varchar REFERENCES OP_SIDING
);

CREATE TABLE IF NOT EXISTS PARAMETER_CATEGORY (
	PCA_id varchar PRIMARY KEY,
	PCA_name varchar
);

CREATE TABLE IF NOT EXISTS PARAMETER (
	PAR_id varchar PRIMARY KEY,
	PAR_value varchar,
	PAR_opvalue varchar,
	PCA_id varchar REFERENCES PARAMETER_CATEGORY,
	ISA_isapplicable IS_APPLICABLE,
	TCA_en TRACK_CATEGORY
);

CREATE TABLE IF NOT EXISTS LOCATION_POINT (
	LOC_id varchar PRIMARY KEY,
	LOC_lon float8,
	LOC_lat float8,
	LOC_distance float8,
	LOC_geom geometry(Point, 4326),
	PAR_id varchar REFERENCES PARAMETER,
	STR_id varchar REFERENCES SOL_TRACK
);


CREATE TABLE IF NOT EXISTS SOL_TRACK_PARAMETER (
	STRP_id varchar PRIMARY KEY,
	PAR_id varchar REFERENCES PARAMETER,
	STR_id varchar REFERENCES SOL_TRACK

);



CREATE TABLE IF NOT EXISTS SOL_TUNNEL_PARAMETER (
	STTP_id varchar PRIMARY KEY,
	PAR_id varchar REFERENCES PARAMETER,
	STU_id varchar REFERENCES SOL_TUNNEL

);



CREATE TABLE IF NOT EXISTS OP_TRACK_PARAMETER (	
	OTRP_id varchar PRIMARY KEY,	
	PAR_id varchar REFERENCES PARAMETER,
	OTR_id varchar REFERENCES OP_TRACK
);



CREATE TABLE IF NOT EXISTS OP_TRACK_TUNNEL_PARAMETER (
	OTUP_id varchar PRIMARY KEY,
	PAR_id varchar REFERENCES PARAMETER,
	OTU_id varchar REFERENCES OP_TRACK_TUNNEL
);



CREATE TABLE IF NOT EXISTS OP_TRACK_PLATFORM_PARAMETER (
	OPLP_id varchar PRIMARY KEY,
	PAR_id varchar REFERENCES PARAMETER,
	OPL_id varchar REFERENCES OP_TRACK_PLATFORM
);

CREATE TABLE IF NOT EXISTS OP_SIDING_PARAMETER (
	OSIP_id varchar PRIMARY KEY,
	PAR_id varchar REFERENCES PARAMETER,
	OSI_id varchar REFERENCES OP_SIDING
);

CREATE TABLE IF NOT EXISTS OP_SIDING_TUNNEL_PARAMETER (
	OSTP_id varchar PRIMARY KEY,
	PAR_id varchar REFERENCES PARAMETER,
	OST_id varchar REFERENCES OP_SIDING_TUNNEL
	);

CREATE TABLE IF NOT EXISTS PARAMETER_FIELD (
	PFI_id varchar PRIMARY KEY,
	PCA_id varchar REFERENCES PARAMETER_CATEGORY	
	);

CREATE TABLE IF NOT EXISTS PARAMETER_CALCULATOR (
	PCL_id varchar PRIMARY KEY,
	PCA_id varchar REFERENCES PARAMETER_CATEGORY
);

CREATE TABLE IF NOT EXISTS TRACK_PARAMETER_RELATION (
	TPR_id varchar PRIMARY KEY,
	PCA_id varchar REFERENCES PARAMETER_CATEGORY,
	TCA_en TRACK_CATEGORY
);


