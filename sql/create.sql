CREATE TABLE IF NOT EXISTS MEMBER (
	MEM_code varchar,
	MEM_version varchar
);

/*
CREATE TABLE RAILWAY_LOCATION (
	RAL_id serial ,
	RAL_distance float8 ,
	RAL_natid varchar ,
	OPP_op bigint ,
	LIN_line bigint 
);



CREATE TABLE OP_TYPE (
	OTY_id serial ,
	OTY_value varchar ,
	OTY_opvalue varchar
);

*/

CREATE TABLE IF NOT EXISTS SECTION_OF_LINE (
	--SOL_id serial ,
	SOL_length float8 ,
	SOL_nature varchar,
	SOL_imcode int ,
	OPP_start varchar ,
	OPP_end varchar ,
	MEM_member varchar ,
	--EXI_date bigint ,
	LIN_line varchar 
);



CREATE TABLE IF NOT EXISTS OPERATIONAL_POINT (
	OPP_name varchar ,
	OPP_uniqueid varchar ,
	OPP_lon float8 ,
	OPP_lat float8 ,
	OPP_taftapcode varchar ,
    	--EXI_date bigint
	--OTY_type bigint ,
	MEM_member varchar
);



CREATE TABLE IF NOT EXISTS OP_TRACK (
	--OTR_id serial ,
    	--EXI_date bigint,
    	--OPP_op varchar, 
	OTR_name varchar ,
	OTR_imcode int

	
);



CREATE TABLE IF NOT EXISTS OP_TUNNEL (
	--OTU_id serial ,
    	--EXI_date bigint ,
    	--OTR_optrack varchar , 
	OTU_name varchar ,
	OTU_imcode int
	
);



CREATE TABLE IF NOT EXISTS OP_PLATFORM (
	--OPL_id serial ,
    	--EXI_date bigint ,
    	--OTR_optrack bigint ,
	OPL_name varchar ,
	OPL_IMCode int


);



CREATE TABLE IF NOT EXISTS SOL_TRACK (
	--STR_id serial ,
    	--SOL_sol bigint ,
	--EXI_date bigint
	STR_name varchar ,
	STR_direction  varchar 

);



CREATE TABLE IF NOT EXISTS SOL_TUNNEL (
	--STU_id serial ,
    	--STR_soltrack bigint ,
	--EXI_date bigint
	STU_name varchar ,
	STU_startlon float8 ,
	STU_startlat float8 ,
	STU_endlon float8 ,
	STU_endlat float8 ,
	STU_imcode int

);




CREATE TABLE IF NOT EXISTS EXISTENCE (
	--EXI_id serial ,
	EXI_start DATE ,
	EXI_end DATE 

);
