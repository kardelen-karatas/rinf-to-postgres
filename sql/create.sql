CREATE TYPE TRACK_CATEGORY AS ENUM(
	'SOL_TRACK',
	'TRACK',
	'TUNNEL',
	'PLATFORM'
);

CREATE TABLE IF NOT EXISTS MEMBER (
	MEM_id varchar PRIMARY KEY,
	MEM_version varchar,
	DOC_id varchar
);

CREATE TABLE IF NOT EXISTS LINE (
	LIN_id varchar PRIMARY KEY,
	LIN_name varchar UNIQUE, 
	MEM_id varchar REFERENCES MEMBER ON DELETE CASCADE
);

CREATE TABLE OP_TYPE (
	OTY_id integer PRIMARY KEY,
	OTY_name varchar
);

CREATE TABLE IF NOT EXISTS OPERATIONAL_POINT (
	OPP_id varchar PRIMARY KEY, --BigAutoField
	OPP_name varchar ,
	OPP_uniqueid varchar UNIQUE,
	OPP_lon float8 ,
	OPP_lat float8 ,
	OPP_geom geometry(Point, 4326),
	OPP_taftapcode varchar , --date
	OPP_date_start varchar, --date
	OPP_date_end varchar,
	OPP_track_nb integer ,
	OPP_tunnel_nb integer ,
	OPP_platform_nb integer ,
	OTY_id int REFERENCES OP_TYPE ON DELETE CASCADE,
	MEM_id varchar REFERENCES MEMBER ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS SECTION_OF_LINE (
	SOL_id varchar PRIMARY KEY,
	SOL_length float8,
	SOL_nature varchar,
	SOL_imcode varchar,
	SOL_date_start varchar ,
	SOL_date_end varchar ,
	SOL_track_nb integer ,
	SOL_tunnel_nb integer ,
	SOL_tunnel_geom geometry(Geometry,4326),
	OPP_start varchar REFERENCES OPERATIONAL_POINT(OPP_uniqueid) ON DELETE CASCADE,
	OPP_end varchar REFERENCES OPERATIONAL_POINT(OPP_uniqueid) ON DELETE CASCADE,
	MEM_id varchar REFERENCES MEMBER ON DELETE CASCADE,
	LIN_id varchar REFERENCES LINE(LIN_name) ON DELETE CASCADE,
	UNIQUE(OPP_start, OPP_end)
);

CREATE TABLE IF NOT EXISTS PARAMETER (
	PAR_id varchar PRIMARY KEY,
	PAR_name varchar,
	PAR_type TRACK_CATEGORY,
	UNIQUE(PAR_name)
);

CREATE TABLE IF NOT EXISTS PARAMETER_DEFINITION (
	PPV_id SERIAL PRIMARY KEY,
	PAR_name varchar UNIQUE,
	PPV_value varchar,
	PPV_optional_value varchar,
	PAR_id varchar REFERENCES PARAMETER ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS OPP_PARAMETER_VALUE (
	OPV_id SERIAL PRIMARY KEY,
	OPV_value VARCHAR,
	OPP_id VARCHAR REFERENCES OPERATIONAL_POINT ON DELETE CASCADE,
	PAR_name VARCHAR,   
	UNIQUE(OPP_id, PAR_name, OPV_value),
	FOREIGN KEY (PAR_name) REFERENCES PARAMETER(PAR_name) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS SOL_PARAMETER_VALUE (
	SPV_id SERIAL PRIMARY KEY,
	SPV_value VARCHAR,  
	SOL_id VARCHAR REFERENCES SECTION_OF_LINE ON DELETE CASCADE, 
	PAR_name VARCHAR ,   
	UNIQUE(SOL_id, PAR_name, SPV_value),
	FOREIGN KEY (PAR_name) REFERENCES PARAMETER(PAR_name) ON DELETE CASCADE
);

