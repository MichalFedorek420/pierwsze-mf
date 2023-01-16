import json
ICAO={
"A":"ALFA",
"B":"BETA",
"C":"CHARLIE",
"D":"DELTA",
"E":"ECHO",
"F":"Foxtrot",
"G":"Golf",
"H":"Hotel",
"I":"India",
"J":"Juliett",
"K":"Kilo",
"L":"Lima",
"M":"Mike",
"N":"November",
"O":"Oscar",
"P":"Papa",
"Q":"Quebec",
"R":"Romeo",
"S":"Sierra",
"T":"Tango",
"U":"Uniform",
"V":"Victor",
"W":"Whiskey",
"X":"X-Ray",
"Y":"Yankee",
"Z":"Zulu"
}
with open("ISAO.TXT", "w") as f:
    json.dump(ICAO,f,indent=4)