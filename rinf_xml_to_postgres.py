import argparse
from lxml import etree
import uuid


def process_ms(ms):
    global MEM_id
    MEM_id = ms.get("Code")
    MEM_version = ms.get("Version")
    MEMBER_STATES_OUTPUT_FILE.write(MS_SQL_TEMPLATE % (MEM_id, MEM_version))



def process_op(op):
    OPP_id = uuid.uuid1()
    OPP_uniqueid = op.find("UniqueOPID").get("Value")
    OPP_name = op.find("OPName").get("Value").replace("'", "''")
    OPP_taftapcode = op.find("OPTafTapCode").get("Value")
    OPP_lon = op.find("OPGeographicLocation").get("Longitude").replace(",", ".")
    OPP_lat = op.find("OPGeographicLocation").get("Latitude").replace(",", ".")
    OPP_date_start = op.get("ValidityDateStart")
    OPP_date_end = op.get("ValidityDateEnd")
    OTY_id = op.find("OPType").get("Value")
    global MEM_id
    OPERATIONAL_POINT_OUTPUT_FILE.write(OP_SQL_TEMPLATE % (OPP_id, OPP_uniqueid, OPP_name,OPP_taftapcode, OPP_lon, OPP_lat, OPP_date_start, OPP_date_end, OTY_id, MEM_id))

    OTY_id = op.find("OPType").get("Value")
    OTY_name = op.find("OPType").get("OptionalValue")
    OP_TYPE_OUTPUT_FILE.write (OP_TYPE_SQL_TEMPLATE % (OTY_id, OTY_name, OTY_id))


    railway_locations = op.findall('OPRailwayLocation')
    for railway_location in railway_locations:
        RAL_id = uuid.uuid1()
        #remonter au niveau de sol et recuperer le LINE and get son ID 
        RAL_distance = railway_location.get ("Kilometer").replace(",", ".")
        RAL_natid = railway_location.get ("NationalIdentNum")
        RAILWAY_LOCATION_OUTPUT_FILE.write (RAILWAY_LOCATION_SQL_TEMPLATE % (RAL_id, RAL_distance, RAL_natid, OPP_id))

    optracks = op.findall('OPTrack')
    for optrack in optracks:
        OTR_id = uuid.uuid1()
        OTR_name = optrack.find('OPTrackIdentification').get("Value").replace("'", "''")
        OTR_imcode = optrack.find('OPTrackIMCode').get("Value")
        OTR_date_start = optrack.get("ValidityDateStart")
        OTR_date_end = optrack.get("ValidityDateEnd")
        OP_TRACK_OUTPUT_FILE.write(OP_TRACK_SQL_TEMPLATE % (OTR_id,OTR_name, OTR_imcode,OTR_date_start,OTR_date_end,OPP_id))
        
        #PARAMETER_CATEGORY
        PCA_id = uuid.uuid1()
        PCA_name = optrack.get("ID")
        PARAMETER_CATEGORY_OUTPUT_FILE.write(PARAMETER_CATEGORY_SQL_TEMPLATE % (PCA_id,PCA_name,PCA_name))
    
        #PARAMETER
        PAR_id = uuid.uuid1()
        PAR_value = optrack.find('OPTrackParameter').get("Value")
        PAR_opvalue = optrack.find('OPTrackParameter').get("OptionalValue")
        ISA_isapplicable = optrack.find('OPTrackParameter').get("IsApplicable")
        TCA_en = 'OP_TRACK'
        #PCA_id = optrack.find('OPTrackParameter').get("ID")
        PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_name))


        #OPTRACK PARAMETER
        OTRP_id = uuid.uuid1()
        OP_TRACK_PARAMETER_OUTPUT_FILE.write(OP_TRACK_PARAMETER_SQL_TEMPLATE % (OTRP_id,PAR_id,OTR_id))
        

        optunnels = optrack.findall('OPTrackTunnel')
        for optunnel in optunnels:
            OTU_id = uuid.uuid1()
            OTU_name = optunnel.find('OPTrackTunnelIdentification').get("Value").replace("'", "''")
            OTU_imcode = optunnel.find('OPTrackTunnelIMCode').get("Value")
            OTU_date_start = optunnel.get("ValidityDateStart")
            OTU_date_end = optunnel.get("ValidityDateEnd")
            OP_TRACK_TUNNEL_OUTPUT_FILE.write(OP_TRACK_TUNNEL_SQL_TEMPLATE % (OTU_id, OTU_name, OTU_imcode,OTU_date_start,OTU_date_end,OTR_id))

            #PARAMETER_CATEGORY
            PCA_id = uuid.uuid1()
            PCA_name = optunnel.get("ID")
            PARAMETER_CATEGORY_OUTPUT_FILE.write(PARAMETER_CATEGORY_SQL_TEMPLATE % (PCA_id,PCA_name,PCA_name))

            #PARAMETER
            PAR_id = uuid.uuid1()
            PAR_value = optrack.find('OPTrackParameter').get("Value")
            PAR_opvalue = optrack.find('OPTrackParameter').get("OptionalValue")
            ISA_isapplicable = optrack.find('OPTrackParameter').get("IsApplicable")
            TCA_en = 'OP_TRACK_TUNNEL'
            #PCA_id = optrack.find('OPTrackParameter').get("ID")
            PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_name))

            #OP_TRACK_TUNNEL PARAMETER
            OTUP_id = uuid.uuid1()
            OP_TRACK_TUNNEL_PARAMETER_OUTPUT_FILE.write(OP_TRACK_TUNNEL_PARAMETER_SQL_TEMPLATE % (OTUP_id,PAR_id,OTU_id))
    

        opplatforms = optrack.findall('OPTrackPlatform')
        for opplatform in opplatforms:
            OPL_id = uuid.uuid1()
            OPL_name = opplatform.find('OPTrackPlatformIdentification').get("Value").replace("'", "''")
            OPL_imcode = opplatform.find('OPTrackPlatformIMCode').get("Value")
            OPL_date_start = opplatform.get("ValidityDateStart")
            OPL_date_end = opplatform.get("ValidityDateEnd")
            OP_TRACK_PLATFORM_OUTPUT_FILE.write(OP_TRACK_PLATFORM_SQL_TEMPLATE % (OPL_id, OPL_name, OPL_imcode,OPL_date_start,OPL_date_end,OTR_id)) 
            
            #PARAMETER_CATEGORY
            PCA_id = uuid.uuid1()
            PCA_name = opplatform.get("ID")
            PARAMETER_CATEGORY_OUTPUT_FILE.write(PARAMETER_CATEGORY_SQL_TEMPLATE % (PCA_id,PCA_name,PCA_name))
            
            #PARAMETER
            PAR_id = uuid.uuid1()
            PAR_value = optrack.find('OPTrackParameter').get("Value")
            PAR_opvalue = optrack.find('OPTrackParameter').get("OptionalValue")
            ISA_isapplicable = optrack.find('OPTrackParameter').get("IsApplicable")
            TCA_en = 'OP_TRACK_PLATFORM'
            #PCA_id = optrack.find('OPTrackParameter').get("ID")
            PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_name))

            #OP_TRACK_PLATFORM PARAMETER
            OPLP_id = uuid.uuid1()
            OP_TRACK_PLATFORM_PARAMETER_OUTPUT_FILE.write(OP_TRACK_PLATFORM_PARAMETER_SQL_TEMPLATE % (OPLP_id,PAR_id,OPL_id))
    

    opsidings = op.findall('OPSiding')
    for opsiding in opsidings:
        OSI_id = uuid.uuid1()
        OPS_name = opsiding.find('OPSidingIdentification').get("Value").replace("'", "''")
        OPS_imcode = opsiding.find('OPSidingIMCode').get("Value")
        OPS_date_start = opsiding.get("ValidityDateStart")
        OPS_date_end = opsiding.get("ValidityDateEnd")
        OP_SIDING_OUTPUT_FILE.write(OP_SIDING_SQL_TEMPLATE % (OSI_id, OPS_name, OPS_imcode,OPS_date_start,OPS_date_end,OPP_id))
        
        
        #PARAMETER
        PAR_id = uuid.uuid1()
        PAR_value = opsiding.find('OPSidingParameter').get("Value")
        PAR_opvalue = opsiding.find('OPSidingParameter').get("OptionalValue")
        ISA_isapplicable = opsiding.find('OPSidingParameter').get("IsApplicable")
        TCA_en = 'OP_SIDING'
        PCA_id = opsiding.find('OPSidingParameter').get("ID")
        PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_id))

        #OP_SIDING PARAMETER
        OSIP_id = uuid.uuid1()
        OP_SIDING_PARAMETER_OUTPUT_FILE.write(OP_SIDING_PARAMETER_SQL_TEMPLATE % (OSIP_id,PAR_id,OSI_id))

        opsidingtunnels = opsiding.findall('OPSidingTunnel')
        for opsidingtunnel in opsidingtunnels:
            OST_id = uuid.uuid1()
            OST_name = opsidingtunnel.find('OPSidingIdentification').get('Value').replace("'", "''")
            OST_imcode = opsidingtunnel.find('OPSidingTunnelIMCode').get("Value")
            OP_SIDING_TUNNEL_OUTPUT_FILE.write(OP_SIDING_TUNNEL_SQL_TEMPLATE % (OST_id,OST_imcode,OST_name,OSI_id))        
            
            #PARAMETER_CATEGORY
            PCA_id = uuid.uuid1()
            PCA_name = opsidingtunnel.get("ID")
            PARAMETER_CATEGORY_OUTPUT_FILE.write(PARAMETER_CATEGORY_SQL_TEMPLATE % (PCA_id,PCA_name,PCA_name))
        
            #PARAMETER
            PAR_id = uuid.uuid1()
            PAR_value = opsidingtunnel.find('OPSidingTunnelParameter').get("Value")
            PAR_opvalue = opsidingtunnel.find('OPSidingTunnelParameter').get("OptionalValue")
            ISA_isapplicable = opsidingtunnel.find('OPSidingTunnelParameter').get("IsApplicable")
            TCA_en = 'OP_SIDING_TUNNEL'
            PCA_id = opsidingtunnel.find('OPSidingTunnelParameter').get("ID")
            PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_id))

            #OP_SIDING_TUNNEL PARAMETER
            OSTP_id = uuid.uuid1()
            OP_SIDING_TUNNEL_PARAMETER_OUTPUT_FILE.write(OP_SIDING_TUNNEL_PARAMETER_SQL_TEMPLATE % (OSTP_id,PAR_id,OST_id))



def process_sol(sol):
    global MEM_id
    SOL_id = uuid.uuid1()
    SOL_imcode = sol.find("SOLIMCode").get("Value")
    SOL_length = sol.find("SOLLength").get("Value").replace(",", ".")
    SOL_nature = sol.find("SOLNature").get("OptionalValue")
    OPP_start = sol.find("SOLOPStart").get("Value")
    OPP_end = sol.find("SOLOPEnd").get("Value")
    LIN_id = sol.find("SOLLineIdentification").get("Value")
    SOL_date_start = sol.get("ValidityDateStart")
    SOL_date_end = sol.get("ValidityDateEnd")
    SECTION_OF_LINE_OUTPUT_FILE.write(SOL_SQL_TEMPLATE % (SOL_id, SOL_length, SOL_nature, SOL_imcode, MEM_id, SOL_date_start, SOL_date_end, LIN_id, OPP_start, OPP_end))

    LIN_id = uuid.uuid1()
    LIN_name = sol.find("SOLLineIdentification").get("Value")
    LINE_OUTPUT_FILE.write(LINE_SQL_TEMPLATE % (LIN_id, LIN_name, MEM_id, LIN_name))

    soltracks = sol.findall('SOLTrack')
    for soltrack in soltracks:
        STR_id = uuid.uuid1()
        STR_name = soltrack.find('SOLTrackIdentification').get("Value").replace("'", "''")
        STR_direction = soltrack.find('SOLTrackDirection').get("Value")
        STR_date_start = soltrack.get("ValidityDateStart")
        STR_date_end = soltrack.get("ValidityDateEnd")
        SOL_TRACK_OUTPUT_FILE.write(SOL_TRACK_SQL_TEMPLATE %
                                (STR_id,STR_name, STR_direction,STR_date_start,STR_date_end,SOL_id))

        soltrack_parameters = soltrack.findall('SOLTrackParameter')
        for soltrack_parameter in soltrack_parameters:

            #PARAMETER_CATEGORY
            PCA_id = uuid.uuid1()
            PCA_name = soltrack_parameter.get("ID")
            PARAMETER_CATEGORY_OUTPUT_FILE.write(PARAMETER_CATEGORY_SQL_TEMPLATE % (PCA_id,PCA_name,PCA_name))


            #PARAMETER
            PAR_id = uuid.uuid1()
            PAR_value = soltrack_parameter.get("Value")
            PAR_opvalue = soltrack_parameter.get("OptionalValue")
            ISA_isapplicable = soltrack_parameter.get("IsApplicable")
            TCA_en = 'SOL_TRACK'
            PCA_id = soltrack_parameter.get("ID")
            PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_id))

            #SOL_TRACK PARAMETER
            STRP_id = uuid.uuid1()
            SOL_TRACK_PARAMETER_OUTPUT_FILE.write(SOL_TRACK_PARAMETER_SQL_TEMPLATE % (STRP_id,PAR_id,STR_id))

            location_points = soltrack_parameter.findall('LocationPoint')
            for location_point in location_points:
                LOC_id = uuid.uuid1()
                LOC_lon = location_point.get('Longitude').replace(",", ".")
                LOC_lat = location_point.get("Latitude").replace(",", ".")
                LOC_distance = location_point.get('Kilometer').replace(",", ".")
                LOCATION_POINT_OUTPUT_FILE.write(LOCATION_POINT_SQL_TEMPLATE % (LOC_id,LOC_lon, LOC_lat,LOC_distance,STR_id,PAR_id))


        soltunnels = soltrack.findall('SOLTunnel')
        for soltunnel in soltunnels:
            STU_id = uuid.uuid1()
            STU_name = soltunnel.find('SOLTunnelIdentification').get("Value").replace("'", "''")
            STU_imcode = soltunnel.find('SOLTunnelIMCode').get("Value")
            STU_startlon = soltunnel.find('SOLTunnelStart').get("Longitude").replace(",", ".")
            STU_startlat = soltunnel.find('SOLTunnelStart').get("Latitude").replace(",", ".")
            STU_endlon = soltunnel.find('SOLTunnelEnd').get("Longitude").replace(",", ".")
            STU_endlat = soltunnel.find('SOLTunnelEnd').get("Latitude").replace(",", ".")
            STU_date_start = soltunnel.get("ValidityDateStart")
            STU_date_end = soltunnel.get("ValidityDateEnd")
            SOL_TUNNEL_OUTPUT_FILE.write(SOL_TUNNEL_SQL_TEMPLATE % (STU_id, STU_name, STU_startlon, STU_startlat, STU_endlon, STU_endlat, STU_imcode,STU_date_start,STU_date_end,STR_id))

            soltunnel_parameters = soltunnel.findall('SOLTunnelParameter')
            for soltunnel_parameter in soltunnel_parameters:

                PCA_id = uuid.uuid1()
                PCA_name = soltunnel_parameter.get("ID")
                PARAMETER_CATEGORY_OUTPUT_FILE.write(PARAMETER_CATEGORY_SQL_TEMPLATE % (PCA_id,PCA_name,PCA_name))

                #PARAMETER
                PAR_id = uuid.uuid1()
                PAR_value = soltunnel_parameter.get("Value")
                PAR_opvalue = soltunnel_parameter.get("OptionalValue")
                ISA_isapplicable = soltunnel_parameter.get("IsApplicable")
                TCA_en = 'SOL_TUNNEL'
                PCA_id = soltunnel_parameter.get("ID")
                PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_id))

                #SOL_TUNEEL PARAMETER
                STTP_id = uuid.uuid1()
                SOL_TUNNEL_PARAMETER_OUTPUT_FILE.write(SOL_TUNNEL_PARAMETER_SQL_TEMPLATE % (STTP_id,PAR_id,STU_id))


def fast_iter(context):

    for event, elem in context:
        if elem.tag == 'MemberStateCode':
            if event == 'end':
                process_ms(elem)
                elem.clear()
        elif elem.tag == 'OperationalPoint':
            if event == 'end':
                process_op(elem)
                elem.clear()
        elif elem.tag == 'SectionOfLine':
            if event == 'end':
                process_sol(elem)
                elem.clear()

    del context


MS_SQL_TEMPLATE = "INSERT INTO MEMBER (MEM_id,MEM_version) VALUES ('%s','%s');\n"

LINE_SQL_TEMPLATE = "INSERT INTO LINE (LIN_id, LIN_name, MEM_id) SELECT '%s','%s','%s' WHERE NOT exists (SELECT 1 FROM LINE WHERE LIN_name = '%s');\n"

OP_TYPE_SQL_TEMPLATE = "INSERT INTO OP_TYPE (OTY_id, OTY_name) SELECT '%s','%s' WHERE NOT exists (SELECT 1 FROM OP_TYPE WHERE OTY_id = '%s');\n"

OP_SQL_TEMPLATE = "INSERT INTO OPERATIONAL_POINT (OPP_id, OPP_uniqueid, OPP_name,OPP_taftapcode, OPP_lon, OPP_lat, OPP_date_start, OPP_date_end, OTY_id, MEM_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');\n"

SOL_SQL_TEMPLATE = "INSERT INTO SECTION_OF_LINE (SOL_id, SOL_length, SOL_nature, SOL_imcode, MEM_id, SOL_date_start, SOL_date_end, LIN_id, OPP_start, OPP_end) VALUES ('%s','%s','%s','%s','%s','%s','%s', (select LIN_id from LINE where LIN_name = '%s'),(select OPP_id from OPERATIONAL_POINT where OPP_uniqueid = '%s'),(select OPP_id from  OPERATIONAL_POINT where OPP_uniqueid = '%s'));\n"

OP_TRACK_SQL_TEMPLATE = "INSERT INTO OP_TRACK (OTR_id,OTR_name, OTR_imcode,OTR_date_start,OTR_date_end,OPP_id) VALUES ('%s','%s','%s','%s','%s','%s');\n"

OP_SIDING_SQL_TEMPLATE = "INSERT INTO OP_SIDING (OSI_id, OSI_name, OSI_imcode, OSI_date_start, OSI_date_end, OPP_id) VALUES ('%s','%s','%s','%s','%s','%s');\n"

SOL_TRACK_SQL_TEMPLATE = "INSERT INTO SOL_TRACK (STR_id,STR_name, STR_direction,STR_date_start,STR_date_end,SOL_id) VALUES ('%s','%s','%s','%s','%s','%s');\n"

RAILWAY_LOCATION_SQL_TEMPLATE = "INSERT INTO RAILWAY_LOCATION (RAL_id, RAL_distance, RAL_natid, OPP_id) VALUES ('%s','%s','%s','%s');\n"

SOL_TUNNEL_SQL_TEMPLATE = "INSERT INTO SOL_TUNNEL (STU_id, STU_name, STU_startlon, STU_startlat, STU_endlon, STU_endlat, STU_imcode,STU_date_start,STU_date_end,STR_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');\n"

OP_TRACK_TUNNEL_SQL_TEMPLATE = "INSERT INTO OP_TRACK_TUNNEL (OTU_id, OTU_name, OTU_imcode,OTU_date_start,OTU_date_end,OTR_id) VALUES ('%s','%s','%s','%s','%s','%s');\n"

OP_TRACK_PLATFORM_SQL_TEMPLATE = "INSERT INTO OP_TRACK_PLATFORM (OPL_id, OPL_name, OPL_imcode,OPL_date_start,OPL_date_end,OTR_id) VALUES ('%s','%s','%s','%s','%s','%s');\n"

OP_SIDING_TUNNEL_SQL_TEMPLATE = "INSERT INTO OP_SIDING_TUNNEL_SPARAMETER (OST_id,OST_imcode,OST_name,OSI_id) VALUES ('%s','%s','%s','%s');\n"

PARAMETER_CATEGORY_SQL_TEMPLATE = "INSERT INTO PARAMETER_CATEGORY (PCA_id,PCA_name) SELECT '%s','%s' WHERE NOT exists (SELECT 1 FROM PARAMETER_CATEGORY WHERE PCA_name = '%s');\n"

PARAMETER_SQL_TEMPLATE = "INSERT INTO PARAMETER (PAR_id,PAR_value,PAR_opvalue,ISA_isapplicable,TCA_en,PCA_id) VALUES ('%s','%s','%s','%s','%s',(select PCA_id from PARAMETER_CATEGORY where PCA_name = '%s'));\n"

LOCATION_POINT_SQL_TEMPLATE = "INSERT INTO LOCATION_POINT (LOC_id, LOC_lon, LOC_lat, LOC_distance, STR_id, PAR_id) VALUES ('%s','%s','%s','%s','%s','%s');\n"

SOL_TRACK_PARAMETER_SQL_TEMPLATE = "INSERT INTO SOL_TRACK_PARAMETER (STRP_id,PAR_id,STR_id) VALUES ('%s','%s','%s');\n"

SOL_TUNNEL_PARAMETER_SQL_TEMPLATE = "INSERT INTO SOL_TUNNEL_PARAMETER (STTP_id,PAR_id,STU_id) VALUES ('%s','%s','%s');\n"

OP_TRACK_PARAMETER_SQL_TEMPLATE = "INSERT INTO OP_TRACK_PARAMETER (OTRP_id,PAR_id,OTR_id) VALUES ('%s','%s','%s');\n"

OP_TRACK_TUNNEL_PARAMETER_SQL_TEMPLATE = "INSERT INTO OP_TRACK_TUNNEL_PARAMETER (OTUP_id,PAR_id,OTU_id) VALUES ('%s','%s','%s');\n"

OP_TRACK_PLATFORM_PARAMETER_SQL_TEMPLATE = "INSERT INTO OP_TRACK_PLATFORM_PARAMETER (OPLP_id,PAR_id,OPL_id) VALUES ('%s','%s','%s');\n"

OP_SIDING_PARAMETER_SQL_TEMPLATE = "INSERT INTO OP_SIDING_PARAMETER_PARAMETER (OSIP_id,PAR_id,OSI_id) VALUES ('%s','%s','%s');\n"

OP_SIDING_TUNNEL_PARAMETER_SQL_TEMPLATE = "INSERT INTO OP_SIDING_TUNNEL_PARAMETER_PARAMETER (OSTP_id,PAR_id,OST_id) VALUES ('%s','%s','%s');\n"

MEM_id = ''
LIN_id = ''


parser = argparse.ArgumentParser(
    description="Extracts data from rinf xml file and outputs sql statements in separate files")
parser.add_argument('--rinf', help="input rinf xml file", required=True)
arguments = parser.parse_args()


MEMBER_STATES_OUTPUT_FILE = open('member_states.sql', 'w')

LINE_OUTPUT_FILE = open('line.sql', 'w')

OP_TYPE_OUTPUT_FILE = open('op_type.sql', 'w')

OPERATIONAL_POINT_OUTPUT_FILE = open('operational_point.sql', 'w')

SECTION_OF_LINE_OUTPUT_FILE = open('section_of_line.sql', 'w')

OP_TRACK_OUTPUT_FILE = open('op_track.sql', 'w')

OP_SIDING_OUTPUT_FILE = open('op_siding.sql', 'w')

SOL_TRACK_OUTPUT_FILE = open('sol_track.sql', 'w')

RAILWAY_LOCATION_OUTPUT_FILE = open('railway_location.sql', 'w')

SOL_TUNNEL_OUTPUT_FILE = open('sol_tunnel.sql', 'w')

OP_TRACK_TUNNEL_OUTPUT_FILE = open('op_track_tunnel.sql', 'w')

OP_TRACK_PLATFORM_OUTPUT_FILE = open('op_track_platform.sql', 'w')

OP_SIDING_TUNNEL_OUTPUT_FILE = open('op_siding_tunnel.sql', 'w')

SOL_TRACK_PARAMETER_OUTPUT_FILE = open('sol_track_parameter.sql', 'w')

SOL_TUNNEL_PARAMETER_OUTPUT_FILE = open('sol_tunnel_parameter.sql', 'w')

LOCATION_POINT_OUTPUT_FILE = open('location_point.sql','w')

OP_TRACK_PARAMETER_OUTPUT_FILE = open('op_track_parameter.sql', 'w')

OP_TRACK_TUNNEL_PARAMETER_OUTPUT_FILE = open('op_track_tunnel_parameter.sql', 'w')

OP_TRACK_PLATFORM_PARAMETER_OUTPUT_FILE = open('op_track_platform_parameter.sql', 'w')

OP_SIDING_PARAMETER_OUTPUT_FILE = open('op_siding_parameter.sql', 'w')

OP_SIDING_TUNNEL_PARAMETER_OUTPUT_FILE = open('op_siding_tunnel_parameter.sql', 'w')

PARAMETER_OUTPUT_FILE = open('parameter.sql', 'w')

PARAMETER_CATEGORY_OUTPUT_FILE = open('parameter_category.sql', 'w')

context = etree.iterparse(arguments.rinf)
fast_iter(context)


MEMBER_STATES_OUTPUT_FILE.close()

LINE_OUTPUT_FILE.close()

OP_TYPE_OUTPUT_FILE.close()

OPERATIONAL_POINT_OUTPUT_FILE.close()

SECTION_OF_LINE_OUTPUT_FILE.close()

SOL_TRACK_OUTPUT_FILE.close()

SOL_TRACK_PARAMETER_OUTPUT_FILE.close()

SOL_TUNNEL_OUTPUT_FILE.close()

SOL_TUNNEL_PARAMETER_OUTPUT_FILE.close()

LOCATION_POINT_OUTPUT_FILE.close()

RAILWAY_LOCATION_OUTPUT_FILE.close()

OP_TRACK_OUTPUT_FILE.close()

OP_TRACK_PARAMETER_OUTPUT_FILE.close()

OP_TRACK_TUNNEL_OUTPUT_FILE.close()

OP_TRACK_TUNNEL_PARAMETER_OUTPUT_FILE.close()

OP_TRACK_PLATFORM_OUTPUT_FILE.close()

OP_TRACK_PLATFORM_PARAMETER_OUTPUT_FILE.close()

OP_SIDING_OUTPUT_FILE .close()

OP_SIDING_PARAMETER_OUTPUT_FILE .close()

OP_SIDING_TUNNEL_OUTPUT_FILE.close()

OP_SIDING_TUNNEL_PARAMETER_OUTPUT_FILE.close()

OP_SIDING_TUNNEL_PARAMETER_OUTPUT_FILE.close()

PARAMETER_OUTPUT_FILE.close()

PARAMETER_CATEGORY_OUTPUT_FILE.close()