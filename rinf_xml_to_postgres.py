import argparse
from lxml import etree


def process_ms(ms):
    global MEM_member
    MEM_member = ms.get("Code")
    MEM_code = ms.get("Code")
    MEM_version = ms.get("Version")
    MEMBER_STATES_OUTPUT_FILE.write(MS_SQL_TEMPLATE % (MEM_code, MEM_version))


def process_railway_location(railway_location):
    global OPP_uniqueid
    global LIN_line
    RAL_distance = railway_location.get ("Kilometer").replace(",", ".")
    RAL_natid = railway_location.get ("NationalIdentNum")
    RAILWAY_LOCATION_OUTPUT_FILE.write (RAILWAY_LOCATION_SQL_TEMPLATE % (RAL_distance, RAL_natid,OPP_uniqueid,LIN_line))


def process_sol(sol):
    global MEM_member
    global LIN_line
    SOL_imcode = sol.find("SOLIMCode").get("Value")
    SOL_length = sol.find("SOLLength").get("Value").replace(",", ".")
    SOL_nature = sol.find("SOLNature").get("OptionalValue")
    OPP_start = sol.find("SOLOPStart").get("Value")
    OPP_end = sol.find("SOLOPEnd").get("Value")
    LIN_line = sol.find("SOLLineIdentification").get("Value")
    SECTION_OF_LINE_OUTPUT_FILE.write(SOL_SQL_TEMPLATE % (
        SOL_length, SOL_nature, SOL_imcode, OPP_start, OPP_end, MEM_member, LIN_line))


    EXI_start = sol.get("ValidityDateStart")
    EXI_end = sol.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))



def process_op(op):
    global MEM_member
    global OPP_uniqueid
    OPP_uniqueid = op.find('UniqueOPID').get("Value")
    OPP_name = op.find('OPName').get("Value").replace("'", "''")
    OPP_taftapcode = op.find('OPTafTapCode').get("Value")
    OPP_lon = op.find('OPGeographicLocation').get(
        "Longitude").replace(",", ".")
    OPP_lat = op.find('OPGeographicLocation').get("Latitude").replace(",", ".")
    OPERATIONAL_POINT_OUTPUT_FILE.write(OP_SQL_TEMPLATE % (
        OPP_name, OPP_uniqueid, OPP_lon, OPP_lat, OPP_taftapcode, MEM_member))


    EXI_start = op.get("ValidityDateStart")
    EXI_end = op.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))


def process_op_track(op_track):
    global OPP_uniqueid
    OTR_name = op_track.find('OPTrackIdentification').get(
        "Value").replace("'", "''")
    OTR_imcode = op_track.find('OPTrackIMCode').get("Value")
    OP_TRACK_OUTPUT_FILE.write(OP_TRACK_SQL_TEMPLATE % (OTR_name, OTR_imcode, OPP_uniqueid))

    #VALIDITY DATE
    EXI_start = op_track.get("ValidityDateStart")
    EXI_end = op_track.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))

    #PARAMETERS
    PAR_name = op_track.find('OPTrackParameter').get("ID")
    PAR_value = op_track.find('OPTrackParameter').get("Value")
    PAR_opvalue = op_track.find('OPTrackParameter').get("OptionalValue")
    ISA_isapplicable = op_track.find('OPTrackParameter').get("IsApplicable")
    TCA_trackcat = 'OP_TRACK'
    PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_name, PAR_value, PAR_opvalue,ISA_isapplicable,TCA_trackcat))



def process_op_tunnel(op_tunnel):
    OTU_name = op_tunnel.find('OPTrackTunnelIdentification').get(
        "Value").replace("'", "''")
    OTU_imcode = op_tunnel.find('OPTrackTunnelIMCode').get("Value")
    OP_TUNNEL_OUTPUT_FILE.write(OP_TUNNEL_SQL_TEMPLATE %
                                (OTU_name, OTU_imcode))

    #VALIDITY DATE
    EXI_start = op_tunnel.get("ValidityDateStart")
    EXI_end = op_tunnel.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))



def process_op_platform(op_platform):
    OPL_name = op_platform.find('OPTrackPlatformIdentification').get(
        "Value").replace("'", "''")
    OPL_imcode = op_platform.find('OPTrackPlatformIMCode').get("Value")
    OP_PLATFORM_OUTPUT_FILE.write(
        OP_PLATFORM_SQL_TEMPLATE % (OPL_name, OPL_imcode))

    #VALIDITY DATE
    EXI_start = op_platform.get("ValidityDateStart")
    EXI_end = op_platform.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))


    #PARAMETER
    PAR_name = op_platform.find('OPTrackPlatformParameter').get("ID")
    PAR_value = op_platform.find('OPTrackPlatformParameter').get("Value")
    PAR_opvalue = op_platform.find('OPTrackPlatformParameter').get("OptionalValue")
    ISA_isapplicable = op_platform.find('OPTrackPlatformParameter').get("IsApplicable")
    TCA_trackcat = 'OP_PLATFORM'
    PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_name, PAR_value, PAR_opvalue,ISA_isapplicable,TCA_trackcat))


def process_sol_track(sol_track):
    STR_name = sol_track.find('SOLTrackIdentification').get(
        "Value").replace("'", "''")
    STR_direction = sol_track.find('SOLTrackDirection').get("Value")
    SOL_TRACK_OUTPUT_FILE.write(SOL_TRACK_SQL_TEMPLATE %
                                (STR_name, STR_direction))


    #VALIDITY DATE
    EXI_start = sol_track.get("ValidityDateStart")
    EXI_end = sol_track.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))


    #PARAMETER
    PAR_name = sol_track.find('SOLTrackParameter').get("ID")
    PAR_value = sol_track.find('SOLTrackParameter').get("Value")
    PAR_opvalue = sol_track.find('SOLTrackParameter').get("OptionalValue")
    ISA_isapplicable = sol_track.find('SOLTrackParameter').get("IsApplicable")
    TCA_trackcat = 'SOL_TRACK'
    PARAMETER_OUTPUT_FILE.write(PARAMETER_SQL_TEMPLATE % (PAR_name, PAR_value, PAR_opvalue,ISA_isapplicable,TCA_trackcat))



def process_sol_tunnel(sol_tunnel):
    STU_name = sol_tunnel.find('SOLTunnelIdentification').get(
        "Value").replace("'", "''")
    STU_imcode = sol_tunnel.find('SOLTunnelIMCode').get("Value")
    STU_startlon = sol_tunnel.find('SOLTunnelStart').get(
        "Longitude").replace(",", ".")
    STU_startlat = sol_tunnel.find('SOLTunnelStart').get(
        "Latitude").replace(",", ".")
    STU_endlon = sol_tunnel.find('SOLTunnelEnd').get(
        "Longitude").replace(",", ".")
    STU_endlat = sol_tunnel.find('SOLTunnelEnd').get(
        "Latitude").replace(",", ".")
    SOL_TUNNEL_OUTPUT_FILE.write(SOL_TUNNEL_SQL_TEMPLATE % (
        STU_name, STU_startlon, STU_startlat, STU_endlon, STU_endlat, STU_imcode))


    #VALIDITY DATE
    EXI_start = sol_tunnel.get("ValidityDateStart")
    EXI_end = sol_tunnel.get("ValidityDateEnd")
    if EXI_start or EXI_end is not None:
        VALIDITY_DATE_OUTPUT_FILE.write(
            VALIDITY_DATE_SQL_TEMPLATE % (EXI_start, EXI_end))



def process_location_point(location_point):
    LOC_lon = location_point.get('Longitude').replace(",", ".")
    LOC_lon = location_point.get('Latitude').replace(",", ".")
    LOC_distance = location_point.get('Kilometer').replace(",", ".")
    LOCATION_POINT_OUTPUT_FILE.write(LOCATION_POINT_SQL_TEMPLATE %
                                (LOC_lon, LOC_lon,LOC_distance))



def fast_iter(context):
    for event, elem in context:
        if elem.tag == 'SectionOfLine':
            if event == 'end':
                process_sol(elem)
                elem.clear()
        elif elem.tag == 'OperationalPoint':
            if event == 'end':
                process_op(elem)
                elem.clear()
        elif elem.tag == 'MemberStateCode':
            if event == 'end':
                process_ms(elem)
                elem.clear()
        elif elem.tag == 'OPTrackPlatform':
            if event == 'end':
                process_op_platform(elem)
                elem.clear()
        elif elem.tag == 'OPTrack':
            if event == 'end':
                process_op_track(elem)
                elem.clear()
        elif elem.tag == 'OPTrackTunnel':
            if event == 'end':
                process_op_tunnel(elem)
                elem.clear()
        elif elem.tag == 'SOLTrack':
            if event == 'end':
                process_sol_track(elem)
                elem.clear()
        elif elem.tag == 'SOLTunnel':
            if event == 'end':
                process_sol_tunnel(elem)
                elem.clear()
        elif elem.tag == 'OPRailwayLocation':
            if event == 'end':
                process_railway_location(elem)
                elem.clear()
        elif elem.tag == 'LocationPoint':
            if event == 'end':
                process_location_point(elem)
                elem.clear()

    del context


MS_SQL_TEMPLATE = "INSERT INTO MEMBER (MEM_code,MEM_version) VALUES ('%s','%s');\n"
SOL_SQL_TEMPLATE = "INSERT INTO SECTION_OF_LINE (SOL_length, SOL_nature, SOL_imcode, OPP_start, OPP_end, MEM_member, LIN_line) VALUES ('%s','%s','%s','%s','%s','%s','%s');\n"
OP_SQL_TEMPLATE = "INSERT INTO OPERATIONAL_POINT (OPP_name, OPP_uniqueid, OPP_lon, OPP_lat, OPP_taftapcode, MEM_member) VALUES ('%s','%s','%s','%s','%s','%s');\n"
OP_TRACK_SQL_TEMPLATE = "INSERT INTO OP_TRACK (OTR_name,OTR_imcode,OPP_uniqueid) VALUES ('%s','%s','%s');\n"
OP_TUNNEL_SQL_TEMPLATE = "INSERT INTO OP_TUNNEL (OTU_name,OTU_imcode) VALUES ('%s','%s');\n"
OP_PLATFORM_SQL_TEMPLATE = "INSERT INTO OP_PLATFORM (OPL_name,OPL_imcode) VALUES ('%s','%s');\n"
SOL_TRACK_SQL_TEMPLATE = "INSERT INTO SOL_TRACK (STR_name,STR_direction) VALUES ('%s','%s');\n"
SOL_TUNNEL_SQL_TEMPLATE = "INSERT INTO SOL_TUNNEL (STU_name,STU_startlon,STU_startlat,STU_endlon,STU_endlat,STU_imcode) VALUES ('%s','%s','%s','%s','%s','%s');\n"
VALIDITY_DATE_SQL_TEMPLATE = "INSERT INTO EXISTENCE (EXI_start,EXI_end) VALUES ('%s','%s');\n"
RAILWAY_LOCATION_SQL_TEMPLATE = "INSERT INTO RAILWAY_LOCATION (RAL_distance,RAL_natid,OPP_uniqueid,LIN_line) VALUES ('%s','%s','%s','%s');\n"
LOCATION_POINT_SQL_TEMPLATE = "INSERT INTO LOCATION_POINT (LOC_lon, LOC_lon,LOC_distance) VALUES ('%s','%s','%s');\n"
PARAMETER_SQL_TEMPLATE = "INSERT INTO PARAMETER (PAR_name, PAR_value,PAR_opvalue, ISA_isapplicable, TCA_trackcat) VALUES ('%s','%s','%s','%s','%s');\n"


MEM_member = ''
OPP_uniqueid = ''
LIN_line = ''


parser = argparse.ArgumentParser(
    description="Extracts data from rinf xml file and outputs sql statements in separate files")
parser.add_argument('--rinf', help="input rinf xml file", required=True)
arguments = parser.parse_args()


SECTION_OF_LINE_OUTPUT_FILE = open('section_of_line.sql', 'w')
SECTION_OF_LINE_COUNT = 0

SOL_TRACK_OUTPUT_FILE = open('section_of_line_track.sql', 'w')
SOL_TRACK_OUTPUT_COUNT = 0

SOL_TUNNEL_OUTPUT_FILE = open('section_of_line_tunnel.sql', 'w')
SOL_TUNNEL_OUTPUT_COUNT = 0

OPERATIONAL_POINT_OUTPUT_FILE = open('operational_point.sql', 'w')
OPERATIONAL_POINT_OUTPUT_COUNT = 0

OP_TRACK_OUTPUT_FILE = open('operational_point_track.sql', 'w')
OP_TRACK_OUTPUT_COUNT = 0

OP_TUNNEL_OUTPUT_FILE = open('operational_point_tunnel.sql', 'w')
OP_TUNNEL_OUTPUT_COUNT = 0

OP_PLATFORM_OUTPUT_FILE = open('operational_point_platform.sql', 'w')
OP_PLATFORM_OUTPUT_COUNT = 0

MEMBER_STATES_OUTPUT_FILE = open('member_states.sql', 'w')
MEMBER_STATES_OUTPUT_COUNT = 0

RAILWAY_LOCATION_OUTPUT_FILE = open('railway_location.sql', 'w')
RAILWAY_LOCATION_OUTPUT_COUNT = 0

VALIDITY_DATE_OUTPUT_FILE = open('validity_date.sql', 'w')
VALIDITY_DATE_OUTPUT_COUNT = 0

LOCATION_POINT_OUTPUT_FILE = open('location_point.sql','w')
LOCATION_POINT_OUTPUT_FILE_COUNT = 0

PARAMETER_OUTPUT_FILE = open('parameter.sql','w')
PARAMETER_OUTPUT_FILE_COUNT = 0


context = etree.iterparse(arguments.rinf)
fast_iter(context)


SECTION_OF_LINE_OUTPUT_FILE.close()
SOL_TRACK_OUTPUT_FILE.close()
SOL_TUNNEL_OUTPUT_FILE.close()
OPERATIONAL_POINT_OUTPUT_FILE.close()
OP_TRACK_OUTPUT_FILE.close()
OP_TUNNEL_OUTPUT_FILE.close()
OP_PLATFORM_OUTPUT_FILE.close()
MEMBER_STATES_OUTPUT_FILE.close()
VALIDITY_DATE_OUTPUT_FILE.close()
RAILWAY_LOCATION_OUTPUT_FILE.close()
PARAMETER_OUTPUT_FILE.close()
