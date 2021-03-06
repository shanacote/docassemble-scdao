from docassemble.base.util import CustomDataType, DAValidationError, word
import re

class Charges(CustomDataType):
    name = 'charges'
    container_class = 'da-charges-container'
    input_class = 'magicsearch multi'
    #input_type = 'charges'
    javascript = """\
    var dataSource;
    if(dataSource){
        $(document).on('daPageLoad', function(){
            $(".magicsearch").magicsearch({
                dataSource: dataSource,
                multiple: true,
                fields: ["firstName","lastName"],
                multiField: "firstName",
                hidden:true,
                id:"id",
                noResult:' ',
                format:"%firstName% · %lastName%"
            });
        });
        $.validator.addMethod('charges', function(value, element, params){
            return true;
        });
    };
    """

    is_object = True
    jq_rule = 'Charges'
    jq_message = 'You need to enter the charges.'

    @classmethod
    def validate(cls, item):
        return True

    @classmethod
    def transform(cls, item):
        dataSource = [
            {
            "firstName":"( A&B ON FAMILY \/ HOUSEHOLD MEMBER SUBSEQUENT)",
            "lastName":"265\/13M\/D"
            },
            {
            "firstName":"2ND DEGREE MURDER",
            "lastName":"265\/1\/A"
            },
            {
            "firstName":"A&AMP;B AGGRAVATED ON PERSON WITH PROTECTIVE ORDER",
            "lastName":"265\/13A\/D***"
            },
            {
            "firstName":"A&AMP;B AGGRAVATED ON PREGNANT PERSON",
            "lastName":"265\/13A\/D**"
            },
            {
            "firstName":"A&AMP;B AGGRAVATED WITH SERIOUS BODILY INJURY",
            "lastName":"265\/13A\/D*"
            },
            {
            "firstName":"A&B ATTEMPT TO DISARM POLICE OFFICER c265 \u00a713D",
            "lastName":"265\/13D\/C"
            },
            {
            "firstName":"A&B BY DISCHARGING FIREARM c265 \u00a715E(a)",
            "lastName":"265\/15E\/A"
            },
            {
            "firstName":"A&B c. 265 s. 13A",
            "lastName":"265.13A"
            },
            {
            "firstName":"A&B c265 \u00a713A",
            "lastName":"265\/13A\/B"
            },
            {
            "firstName":"A&B IN VIOLATION OF RESTRAINING ORDER c265 \u00a713A(b)",
            "lastName":"265\/13A\/F"
            },
            {
            "firstName":"A&B ON +60\/DISABLED c265 \u00a713K\/F",
            "lastName":"265\/13K\/F"
            },
            {
            "firstName":"A&B ON +60\/DISABLED WITH INJURY c265 \u00a713K(b)",
            "lastName":"265\/13K\/A"
            },
            {
            "firstName":"A&B ON +60\/DISABLED WITH SERIOUS INJURY c265 \u00a713K(c)",
            "lastName":"265\/13K\/B"
            },
            {
            "firstName":"A&B ON AMBULANCE PERSONNEL c265 \u00a713I",
            "lastName":"265\/13I\/B"
            },
            {
            "firstName":"A&B ON CHILD TO JOIN CONSPIRACY c265 \u00a744",
            "lastName":"265\/44\/A"
            },
            {
            "firstName":"A&B ON CHILD WITH INJURY c. 265 s. 13J",
            "lastName":"265.13J"
            },
            {
            "firstName":"A&B ON CHILD WITH INJURY c265 \u00a713J(b)",
            "lastName":"265\/13J\/A"
            },
            {
            "firstName":"A&B ON CHILD WITH SUBSTANTIAL INJURY c. 265 s. 13J",
            "lastName":"265.13J"
            },
            {
            "firstName":"A&B ON CHILD WITH SUBSTANTIAL INJURY c265 \u00a713J(b)",
            "lastName":"265\/13J\/B"
            },
            {
            "firstName":"A&B ON CORRECTION OFFICER c. 127 s. 38B",
            "lastName":"127.38B"
            },
            {
            "firstName":"A&B ON CORRECTIONAL OFFICER c127 \u00a738B",
            "lastName":"127\/38B"
            },
            {
            "firstName":"A&B ON ELDER (60+)\/DISABLED PERSON; BODILY INJURY c. 265 s. 13K(b)",
            "lastName":"265.13K(b)"
            },
            {
            "firstName":"A&B ON ELDER (60+)\/DISABLED PERSON; SERIOUS BODILY INJURY c. 265 s. 13K(c)",
            "lastName":"265.13K(c)"
            },
            {
            "firstName":"A&B ON FAMILY\/HOUSEHOLD MEMBER c265 \u00a713M",
            "lastName":"265\/13M"
            },
            {
            "firstName":"A&B ON POLICE OFFICER c265 \u00a713D",
            "lastName":"265\/13D\/A"
            },
            {
            "firstName":"A&B ON POLICE OFFICER, SERIOUS BODILY INJURY c265 \u00a713D",
            "lastName":"265\/13D\/D"
            },
            {
            "firstName":"A&B ON PUBLIC EMPLOYEE c. 265 s. 13D",
            "lastName":"265.13D"
            },
            {
            "firstName":"A&B ON PUBLIC EMPLOYEE c265 \u00a713D",
            "lastName":"265\/13D\/B"
            },
            {
            "firstName":"A&B ON RETARDED PERSON c. 265 s. 13F",
            "lastName":"265.13F"
            },
            {
            "firstName":"A&B ON RETARDED PERSON c265 \u00a713F",
            "lastName":"265\/13F\/C"
            },
            {
            "firstName":"A&B OR PROPERTY DAMAGE TO INTIMIDATE FOR RACE\/RELIGION c. 265 s. 39(a)",
            "lastName":"265.39(a)"
            },
            {
            "firstName":"A&B OR PROPERTY DAMAGE TO INTIMIDATE FOR RACE\/RELIGION, BODILY INJURY  c. 265 s. 39(b)",
            "lastName":"265.39(b)"
            },
            {
            "firstName":"A&B OR PROPERTY DAMAGE TO INTIMIDATE FOR RACE\/RELIGION, BODILY INJURY, ARMED  c. 265 s. 39(b)",
            "lastName":"265.39(b)"
            },
            {
            "firstName":"A&B TO COLLECT LOAN c. 265 s. 13C",
            "lastName":"265.13C"
            },
            {
            "firstName":"A&B TO COLLECT LOAN c265 \u00a713C",
            "lastName":"265\/13C\/A"
            },
            {
            "firstName":"A&B TO COLLECT LOAN, SUBSQ.OFF. c265 \u00a713C",
            "lastName":"265\/13C\/B"
            },
            {
            "firstName":"A&B TO INTIMIDATE c265 \u00a739(a)",
            "lastName":"265\/39\/B"
            },
            {
            "firstName":"A&B TO INTIMIDATE, WITH BODILY INJURY c265 \u00a739(b)",
            "lastName":"265\/39\/D"
            },
            {
            "firstName":"A&B TO INTIMIDATE, WITH BODILY INJURY, ARMED c265 \u00a739(b)",
            "lastName":"265\/39\/E"
            },
            {
            "firstName":"A&B UPON PREGNANT PERSON c265 \u00a713A(b)",
            "lastName":"265\/13A\/E"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON  c265 \u00a715A(b)",
            "lastName":"265\/15A\/A"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON +60 c. 265 s. 15A(a)",
            "lastName":"265.15A(a)"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON +60 c. 265 s. 15A(a) ",
            "lastName":"265.15A(a)"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON +60 c265 \u00a715A(a)",
            "lastName":"265\/15A\/B"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON +60, SUBSQ.OFF c. 265 s. 15A(a)",
            "lastName":"265.15A(a)"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON +60, SUBSQ.OFF c265 \u00a715A(a)",
            "lastName":"265\/15A\/C"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON c. 265 s. 15A(b)",
            "lastName":"265.15A(b)"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON c. 265 s. 15A(b) ",
            "lastName":"265.15A(b)"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON c265 \u00a715A(b)",
            "lastName":"265\/15A\/A"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON CAUSING SERIOUS BODILY INJURY c265 \u00a715A(c)",
            "lastName":"265\/15A\/D"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON IN VIOLATION OF RESTRAINING ORDER c265 \u00a715A(c)",
            "lastName":"265\/15A\/F"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON UPON PREGNANT PERSON c265 \u00a715A(c)",
            "lastName":"265\/15A\/E"
            },
            {
            "firstName":"A&B WITH DANGEROUS WEAPON, CHILD UNDER 14 c265 \u00a715A(c)(iv)",
            "lastName":"265\/15A\/C4"
            },
            {
            "firstName":"A&B, AGGRAVATED c265 \u00a713A(b)",
            "lastName":"265\/13A\/D"
            },
            {
            "firstName":"A&B,CAUSING SERIOUS BODILY INJURY  c265 \u00a713A(b)",
            "lastName":"265\/13A\/C"
            },
            {
            "firstName":"A&B\/ASSAULT ON AMBULANCE PERSONNEL c. 265 s. 13I",
            "lastName":"265.13I"
            },
            {
            "firstName":"A&F INQUIRY, DISTURB, OR WITNESS FAIL TESTIFY AT c. 7 s. 11",
            "lastName":"7.11"
            },
            {
            "firstName":"AAND B",
            "lastName":"265\/13A"
            },
            {
            "firstName":"AAND B BY DANGEROUS WEAPON",
            "lastName":"265\/15A"
            },
            {
            "firstName":"AAND B ON A CHILD",
            "lastName":"265\/13J"
            },
            {
            "firstName":"AAND B ON AN ELDERLY OR HANDIC",
            "lastName":"265\/13K"
            },
            {
            "firstName":"AAND B ON POLICE OFFICER",
            "lastName":"265\/13D"
            },
            {
            "firstName":"ABANDON MV c90 \u00a722B(a)",
            "lastName":"90\/22B\/A"
            },
            {
            "firstName":"ABANDON MV, SUBSQ.OFF. c90 \u00a722B(a)",
            "lastName":"90\/22B\/B"
            },
            {
            "firstName":"ABANDONED\/STOLEN MV, IMPROP REMOVE c90 \u00a724H",
            "lastName":"90\/24H\/A"
            },
            {
            "firstName":"ABANDONED\/STOLEN\/CRUSHED MV, UNREGISTERED OR IMPROPER REMOVAL c. 90 s. 24H",
            "lastName":"90.24H"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER VIOL, RETALIATORY c209A \u00a77",
            "lastName":"209A\/7\/B"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER, VIOL PROBATE CT c. 208 s. 34C",
            "lastName":"208.34C"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER, VIOL PROBATE CT c208 \u00a734C",
            "lastName":"208\/34C"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER, VIOLATE c. 209A s. 3B",
            "lastName":"209A.3B"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER, VIOLATE c. 209A s. 7",
            "lastName":"209A.7"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER, VIOLATE c209A \u00a77",
            "lastName":"209A\/7"
            },
            {
            "firstName":"ABUSE PREVENTION ORDER, VIOLATE, RETALIATION FOR NON-SUPPORT c. 209A s. 7",
            "lastName":"209A.7"
            },
            {
            "firstName":"ACCESSORY AFTER THE FACT c. 274 s. 4",
            "lastName":"274.4"
            },
            {
            "firstName":"ACCESSORY AFTER THE FACT c274 \u00a74",
            "lastName":"274\/4"
            },
            {
            "firstName":"ACCESSORY BEFORE THE FACT c. 274 s. 2",
            "lastName":"274.2"
            },
            {
            "firstName":"ACCESSORY BEFORE THE FACT c274 \u00a72",
            "lastName":"274\/2"
            },
            {
            "firstName":"ACCIDENT REPORT, FAIL FILE * c90 \u00a726",
            "lastName":"90\/26"
            },
            {
            "firstName":"ACCOST\/ANNOY PERSON OF OPPOSITE SEX c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"ACCOST\/ANNOY PERSON OF OPPOSITE SEX c272 \u00a753",
            "lastName":"272\/53\/D"
            },
            {
            "firstName":"ACETYL FENTANYL, TRAFFICKING IN, 200 GRAMS OR MORE c94C \u00a732E(c)",
            "lastName":"94C\/32E\/CC"
            },
            {
            "firstName":"ADMISSION OR RAILROAD TICKET, FORGE c. 267 s. 2",
            "lastName":"267.2"
            },
            {
            "firstName":"ADMISSION OR RAILROAD TICKET, UTTER FALSE c. 267 s. 6",
            "lastName":"267.6"
            },
            {
            "firstName":"ADMISSION TICKET, FORGE c267 \u00a72",
            "lastName":"267\/2\/B"
            },
            {
            "firstName":"ADMISSION TICKET, UTTER FALSE c267 \u00a76",
            "lastName":"267\/6\/B"
            },
            {
            "firstName":"AFFRAY",
            "lastName":"COMMON LAW"
            },
            {
            "firstName":"AFFRAY",
            "lastName":"12412|277-39"
            },
            {
            "firstName":"AFFRAY (Common Law)",
            "lastName":"COMLAW1"
            },
            {
            "firstName":"AFFRAY c. 275 s. 14",
            "lastName":"275 . 14"
            },
            {
            "firstName":"AFTERMARKET LIGHTING, NONCOMPLIANT * 540 CMR \u00a722.07",
            "lastName":"540CMR2207"
            },
            {
            "firstName":"AIRCRAFT OPERATION, INTERFERE WITH c90 \u00a740",
            "lastName":"90\/40\/C"
            },
            {
            "firstName":"AIRCRAFT OPERATION, UNLICENSED c. 90 s. 47",
            "lastName":"90.47"
            },
            {
            "firstName":"AIRPORT RUNWAY, STRUCTURE TOO HIGH NEAR c. 90 s. 35B",
            "lastName":"90.35B"
            },
            {
            "firstName":"AIRPORT SECURITY VIOLATION c269 \u00a712F",
            "lastName":"269\/12F"
            },
            {
            "firstName":"ALCOHOL FROM OPEN CONTAINER IN MV, DRINK c90 \u00a724I",
            "lastName":"90\/24I"
            },
            {
            "firstName":"ALLOWING A MV TO REMAIN UNATTENDED",
            "lastName":"155"
            },
            {
            "firstName":"ALTER, FORGE, OR COUNTERFEIT CERTIFICATE OF TITLE OR SALVAGE TITLE c. 90D s. 32(a)",
            "lastName":"90D.32(a)"
            },
            {
            "firstName":"AMMUNITION OF UNLAWFUL CALIBER c. 131 s. 67",
            "lastName":"131.67"
            },
            {
            "firstName":"AMMUNITION OF UNLAWFUL CALIBER c131 \u00a767",
            "lastName":"131\/67\/B"
            },
            {
            "firstName":"AMMUNITION UNATTENDED c269 \u00a710(h)(2)",
            "lastName":"269\/10\/SS"
            },
            {
            "firstName":"AMMUNITION WITHOUT FID CARD, POSSESS (POSS AMMO)",
            "lastName":"269\/10\/G*"
            },
            {
            "firstName":"AMMUNITION, POSSESS c269 \u00a710(h)",
            "lastName":"269\/10\/A2"
            },
            {
            "firstName":"AMMUNITION, POSSESS WO FID CARD c269 \u00a710\/TT",
            "lastName":"269\/10\/TT"
            },
            {
            "firstName":"AMMUNITION, POSSESS WO FID CARD, SUBSQ.OFF.  c269 \u00a710\/TT",
            "lastName":"269\/10\/UU"
            },
            {
            "firstName":"AMMUNITION, POSSESSION OF c. 269 s. 10H",
            "lastName":"269. 10H"
            },
            {
            "firstName":"AMMUNITION, UNLICENSED SALE OF c. 140 s. 122B",
            "lastName":"140.122B"
            },
            {
            "firstName":"AMMUNITION, UNLICENSED SALE OF c140 \u00a7122B",
            "lastName":"140\/122B"
            },
            {
            "firstName":"ANIMAL FIGHT, KEEP\/PROMOTE c272 \u00a794",
            "lastName":"272\/94"
            },
            {
            "firstName":"ANIMAL QUARANTINE VIOLATION c131 \u00a725C",
            "lastName":"131\/25C"
            },
            {
            "firstName":"ANIMAL, ALLOW TO TRESPASS c266 \u00a7118",
            "lastName":"266\/118"
            },
            {
            "firstName":"ANIMAL, CRUELTY TO BY CUSTODIAN c272 \u00a777",
            "lastName":"272\/77\/B"
            },
            {
            "firstName":"ANIMAL, CRUELTY TO c. 272 s. 77",
            "lastName":"272.77"
            },
            {
            "firstName":"ANIMAL, CRUELTY TO c272 \u00a777",
            "lastName":"272\/77\/A"
            },
            {
            "firstName":"ANIMAL, KILL IN DECOMPRESSION CHAMBER c272 \u00a780E",
            "lastName":"272\/80E"
            },
            {
            "firstName":"ANIMAL, KILL\/MAIM\/POISON c. 266 s. 112",
            "lastName":"266.112"
            },
            {
            "firstName":"ANIMAL, KILL\/MAIM\/POISON c266 \u00a7112",
            "lastName":"266\/112"
            },
            {
            "firstName":"ANIMAL, POSSESS WITHOUT LIC. c. 131 s. 25",
            "lastName":"131.25"
            },
            {
            "firstName":"ANIMAL, POSSESS WITHOUT LICENSE c131 \u00a725",
            "lastName":"131\/25\/B"
            },
            {
            "firstName":"ARCHITECT VIOLATION c. 112 s. 60O",
            "lastName":"112.60O"
            },
            {
            "firstName":"ARMED ASSLT W\/ INT TO MURDER",
            "lastName":"265\/18"
            },
            {
            "firstName":"ARMED CAREER CRIMINAL  c269 \u00a710",
            "lastName":"269C\/10"
            },
            {
            "firstName":"ARMED ROBBERY c. 265 \u00a7 17",
            "lastName":"265\/17"
            },
            {
            "firstName":"ARSENIC TEST, FAIL FURNISH SAMPLE FOR c270 \u00a711",
            "lastName":"270\/11"
            },
            {
            "firstName":"ARSENIC, DISTRIBUTE TOYS\/CANDY WITH c270 \u00a710",
            "lastName":"270\/10"
            },
            {
            "firstName":"ARSON OF DWELLING HOUSE c. 266 s. 1",
            "lastName":"266.1"
            },
            {
            "firstName":"ARSON OF DWELLING HOUSE c266 \u00a71",
            "lastName":"266\/1"
            },
            {
            "firstName":"ARSON OF DWELLING HOUSE, ATTEMPTED c266 \u00a75A",
            "lastName":"266\/5A\/A"
            },
            {
            "firstName":"ASSAULT  AGGRAVATED ON PREGNANT PERSON",
            "lastName":"265\/13A\/C**"
            },
            {
            "firstName":"ASSAULT (209A)",
            "lastName":"12313|265:20"
            },
            {
            "firstName":"ASSAULT & BATTERY ON CHILD, COERCE CONSPIRACY c. 265 s. 44",
            "lastName":"265.44"
            },
            {
            "firstName":"ASSAULT c. 265 s. 13A",
            "lastName":"265.13A"
            },
            {
            "firstName":"ASSAULT c265 \u00a713A",
            "lastName":"265\/13A\/A"
            },
            {
            "firstName":"ASSAULT IN DWELLING, ARMED c. 265 s. 18A",
            "lastName":"265.18A"
            },
            {
            "firstName":"ASSAULT IN DWELLING, ARMED c265 \u00a718A",
            "lastName":"265\/18A"
            },
            {
            "firstName":"ASSAULT IN DWELLING, ARMED, FIREARM c. 265 s. 18A",
            "lastName":"265.18A"
            },
            {
            "firstName":"ASSAULT IN DWELLING, FIREARM-ARMED c265 \u00a718A",
            "lastName":"265\/18A\/B"
            },
            {
            "firstName":"ASSAULT ON AMBULANCE PERSONNEL c265 \u00a713I",
            "lastName":"265\/13I\/A"
            },
            {
            "firstName":"ASSAULT ON FAMILY\/HOUSEHOLD MEMBER c265 \u00a713M(b)",
            "lastName":"265\/13M\/A"
            },
            {
            "firstName":"ASSAULT ON FAMILY\/HOUSEHOLD MEMBER, SUBSQ.OFF c265 \u00a713M(b)",
            "lastName":"265\/13M\/C"
            },
            {
            "firstName":"ASSAULT OR AAND B ON EMT\/AMB O",
            "lastName":"265\/13I"
            },
            {
            "firstName":"ASSAULT TO COMMIT FELONY c. 265 s. 29",
            "lastName":"265.29"
            },
            {
            "firstName":"ASSAULT TO COMMIT FELONY c265 \u00a729",
            "lastName":"265\/29"
            },
            {
            "firstName":"ASSAULT TO INTIMIDATE c265 \u00a739(a)",
            "lastName":"265\/39\/A"
            },
            {
            "firstName":"ASSAULT TO MAIM c265 \u00a714",
            "lastName":"265\/14\/B"
            },
            {
            "firstName":"ASSAULT TO MAIM c265 \u00a715",
            "lastName":"265\/15\/B"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, ARMED c. 265 s. 18(a)",
            "lastName":"265.18(a)"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, ARMED c265 \u00a718(a)",
            "lastName":"265\/18\/A"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, ARMED, FIREARM c. 265 s. 18(a)",
            "lastName":"265.18(a)"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, ARMED, FIREARM, SUBSQ. OFF. c. 265 s. 18(a)",
            "lastName":"265.18(a)"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, ARMED, SUBSQ.OFF. c265 \u00a718(a)",
            "lastName":"265\/18\/B"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, FIREARM-ARMED c265 \u00a718(a)",
            "lastName":"265\/18\/G"
            },
            {
            "firstName":"ASSAULT TO MURDER +60, FIREARM-ARMED, SUBSQ.OFF. c265 \u00a718(a)",
            "lastName":"265\/18\/H"
            },
            {
            "firstName":"ASSAULT TO MURDER c265 \u00a715",
            "lastName":"265\/15\/A"
            },
            {
            "firstName":"ASSAULT TO MURDER OR MAIM c. 265 s. 15",
            "lastName":"265.15"
            },
            {
            "firstName":"ASSAULT TO MURDER, ARMED c. 265 s. 18(b)",
            "lastName":"265.18(b)"
            },
            {
            "firstName":"ASSAULT TO MURDER, ARMED c265 \u00a718(b)",
            "lastName":"265\/18\/C"
            },
            {
            "firstName":"ASSAULT TO MURDER, ARMED, FIREARM c. 265 s. 18(b)",
            "lastName":"265.18(b)"
            },
            {
            "firstName":"ASSAULT TO MURDER, FIREARM-ARMED c265 \u00a718(b)",
            "lastName":"265\/18\/J"
            },
            {
            "firstName":"ASSAULT TO RAPE c. 265 s. 24",
            "lastName":"265.24"
            },
            {
            "firstName":"ASSAULT TO RAPE c265 \u00a724",
            "lastName":"265\/24\/A"
            },
            {
            "firstName":"ASSAULT TO RAPE CHILD c. 265 s. 24B",
            "lastName":"265.24B"
            },
            {
            "firstName":"ASSAULT TO RAPE CHILD c265 \u00a724B",
            "lastName":"265\/24B\/A"
            },
            {
            "firstName":"ASSAULT TO RAPE, ARMED, FIREARM c. 265 s. 24",
            "lastName":"265.24"
            },
            {
            "firstName":"ASSAULT TO RAPE, FIREARM-ARMED c265 \u00a724",
            "lastName":"265\/24\/C"
            },
            {
            "firstName":"ASSAULT TO ROB +60, ARMED",
            "lastName":"265\/18\/D"
            },
            {
            "firstName":"ASSAULT TO ROB +60, ARMED c. 265 s. 18(a)",
            "lastName":"265.18(a)"
            },
            {
            "firstName":"ASSAULT TO ROB +60, ARMED, FIREARM c. 265 s. 18(a)",
            "lastName":"265.18(a)"
            },
            {
            "firstName":"ASSAULT TO ROB +60, ARMED, SUBSQ. OFF. c. 265 s. 18(a)",
            "lastName":"265.18(a)"
            },
            {
            "firstName":"ASSAULT TO ROB +60, FIREARM-ARMED c265 \u00a718(a)",
            "lastName":"265\/18\/K"
            },
            {
            "firstName":"ASSAULT TO ROB, ARMED c. 265 s. 18(b)",
            "lastName":"265.18(b)"
            },
            {
            "firstName":"ASSAULT TO ROB, ARMED c265 \u00a718(b)",
            "lastName":"265\/18\/F"
            },
            {
            "firstName":"ASSAULT TO ROB, ARMED, FIREARM c. 265 s. 18(b)",
            "lastName":"265.18(b)"
            },
            {
            "firstName":"ASSAULT TO ROB, FIREARM-ARMED c265 \u00a718(b)",
            "lastName":"265\/18\/M"
            },
            {
            "firstName":"ASSAULT TO ROB, UNARMED c. 265 s. 20",
            "lastName":"265.2"
            },
            {
            "firstName":"ASSAULT TO ROB, UNARMED c265 \u00a720",
            "lastName":"265\/20"
            },
            {
            "firstName":"ASSAULT W\/DANGEROUS WEAPON +60 c. 265 s. 15B(a)",
            "lastName":"265.15B(a)"
            },
            {
            "firstName":"ASSAULT W\/DANGEROUS WEAPON +60 c265 \u00a715B(a)",
            "lastName":"265\/15B\/B"
            },
            {
            "firstName":"ASSAULT W\/DANGEROUS WEAPON +60, SUBSQ. c265 \u00a715B(a)",
            "lastName":"265\/15B\/C"
            },
            {
            "firstName":"ASSAULT W\/DANGEROUS WEAPON +60, SUBSQ. OFF. c. 265 s. 15B(a)",
            "lastName":"265.15B(a)"
            },
            {
            "firstName":"ASSAULT W\/DANGEROUS WEAPON c. 265 s. 15B(b)",
            "lastName":"265.15B(b)"
            },
            {
            "firstName":"ASSAULT W\/DANGEROUS WEAPON c265 \u00a715B(b)",
            "lastName":"265\/15B\/A"
            },
            {
            "firstName":"ASSAULT WEAPON, SELL\/POSSESS c. 140 s. 131M",
            "lastName":"140.131M"
            },
            {
            "firstName":"ASSAULT WEAPON, SELL\/POSSESS c140 \u00a7131M",
            "lastName":"140\/131M\/A"
            },
            {
            "firstName":"ASSAULT WEAPON, SELL\/POSSESS, SUBSQ. c. 140 s. 131M",
            "lastName":"140.131M"
            },
            {
            "firstName":"ASSAULT WITH HYPODERMIC c265 \u00a715C\/A",
            "lastName":"265\/15C\/A"
            },
            {
            "firstName":"ASSAULT, VIOL ABUSE PREVENTION ORDER c265 \u00a713A(b)",
            "lastName":"265\/13A\/CB"
            },
            {
            "firstName":"ASSLT BY DANG WEAP",
            "lastName":"265\/15B"
            },
            {
            "firstName":"ASSLT W\/ INT TO RAPE",
            "lastName":"265\/24"
            },
            {
            "firstName":"ASSOCIATION MEMBER EMBEZZLE +$250 c. 266 s. 59 ",
            "lastName":"266.59"
            },
            {
            "firstName":"ASSOCIATION MEMBER EMBEZZLE +$250 c266 \u00a759 & \u00a730(1)",
            "lastName":"266\/59\/A"
            },
            {
            "firstName":"ASSOCIATION MEMBERSHIP, FALSELY SOLICIT c266 \u00a771",
            "lastName":"266\/71"
            },
            {
            "firstName":"ASSOCIATION NAME, FALSELY USE\/MIMIC c266 \u00a771A",
            "lastName":"266\/71A"
            },
            {
            "firstName":"ASSOCIATION OFFICER EMBEZZLE +$250 c266 \u00a758 & \u00a730(1)",
            "lastName":"266\/58\/A"
            },
            {
            "firstName":"ATTEMPT TO BURN BOAT\/MOTOR VEHICLE\/PERSONALTY (AS ENUMERATED IN c. 266 s. 5) c. 266 s. 5A",
            "lastName":"266.5A"
            },
            {
            "firstName":"ATTEMPT TO BURN PUBLIC BUILDING (AS ENUMERATED IN c. 266 s. 2) c. 266 s. 5A",
            "lastName":"266.5A"
            },
            {
            "firstName":"ATTEMPT TO COMMIT CRIME c. 274 s. 6 - < 5 Year Felony or Misdemeanor",
            "lastName":"274.6"
            },
            {
            "firstName":"ATTEMPT TO COMMIT CRIME c. 274 s. 6 - 5 year felony or greater",
            "lastName":"274.6"
            },
            {
            "firstName":"ATTEMPT TO COMMIT CRIME c. 274 s. 6 - Larceny ",
            "lastName":"274.6"
            },
            {
            "firstName":"ATTEMPT TO COMMIT CRIME c274 \u00a76",
            "lastName":"274\/6"
            },
            {
            "firstName":"ATTEMPT TO COMMIT CRIME PUNISHABLE BY DEATH c. 274 s. 6 ",
            "lastName":"274.6"
            },
            {
            "firstName":"ATTEMPTED A&B BY DISCHARGING A FIREARM c265 \u00a715F(a)",
            "lastName":"265\/15F\/A"
            },
            {
            "firstName":"ATTEMPTED ARSON OF DWELLING HOUSE (AS ENUMERATED IN c. 266 s. 1) c. 266 s. 5A",
            "lastName":"266.5A"
            },
            {
            "firstName":"ATTEMPTED EXTORTION",
            "lastName":"265\/25"
            },
            {
            "firstName":"ATTEMPTED LARCENY BY CHECK c266 \u00a737",
            "lastName":"266\/37\/C"
            },
            {
            "firstName":"B&AMP;E DAYTIME FOR FELONY",
            "lastName":"266\/18"
            },
            {
            "firstName":"B&E DAYTIME FOR FELONY c266 \u00a718",
            "lastName":"266\/18\/B"
            },
            {
            "firstName":"B&E DAYTIME FOR FELONY, ARMED c266 \u00a718",
            "lastName":"266\/18\/D"
            },
            {
            "firstName":"B&E DAYTIME FOR FELONY, ARMED, PERSON IN FEAR c266 \u00a717",
            "lastName":"266\/17\/D"
            },
            {
            "firstName":"B&E DAYTIME FOR FELONY, PERSON IN FEAR c266 \u00a717",
            "lastName":"266\/17\/B"
            },
            {
            "firstName":"B&E DAYTIME OR ENTER AT NIGHT, FOR FELONY, ARMED, PERSON IN FEAR c. 266 s. 17",
            "lastName":"266.17"
            },
            {
            "firstName":"B&E DAYTIME OR ENTER AT NIGHT, FOR FELONY, PERSON IN FEAR c. 266 s. 17",
            "lastName":"266.17"
            },
            {
            "firstName":"B&E DAYTIME, ARMED, FIREARM, FOR FELONY c. 266 s. 18",
            "lastName":"266.18"
            },
            {
            "firstName":"B&E DAYTIME, FOR FELONY c. 266 s. 18",
            "lastName":"266.18"
            },
            {
            "firstName":"B&E FOR MISDEMEANOR c. 266 s. 16A",
            "lastName":"266.16A"
            },
            {
            "firstName":"B&E FOR MISDEMEANOR c266 \u00a716A",
            "lastName":"266\/16A"
            },
            {
            "firstName":"B&E NIGHTTIME FOR FELONY c266 \u00a716",
            "lastName":"266\/16\/A"
            },
            {
            "firstName":"B&E NIGHTTIME FOR FELONY VEHICLE c266 \u00a716",
            "lastName":"266\/16\/A1"
            },
            {
            "firstName":"B&E NIGHTTIME FOR FELONY\/B&E, OR ATTEMPT, DEPOSITORY c. 266 s. 16",
            "lastName":"266.16"
            },
            {
            "firstName":"B&E VEHICLE\/BOAT DAYTIME FOR FELONY",
            "lastName":"266\/18\/E"
            },
            {
            "firstName":"B&E VEHICLE\/BOAT NIGHTTIME FOR FELONY",
            "lastName":"266\/16\/D"
            },
            {
            "firstName":"BADGE, USE WITHOUT AUTHORITY c268 \u00a735",
            "lastName":"268\/35\/B"
            },
            {
            "firstName":"BAND E NIGHT W\/ INT.TO COM. FE",
            "lastName":"266\/16"
            },
            {
            "firstName":"BANK BILL PAPER, LARCENY OF c. 266 s. 42",
            "lastName":"266.42"
            },
            {
            "firstName":"BANK BILL PAPER, LARCENY OF c266 \u00a742",
            "lastName":"266\/42"
            },
            {
            "firstName":"BANK HOLDING COMPANY RECORD, FALSE c167A \u00a76",
            "lastName":"167A\/6\/A"
            },
            {
            "firstName":"BANK OFFICER\/EMPLOYEE, MISCONDUCT BY c266 \u00a753A",
            "lastName":"266\/53A"
            },
            {
            "firstName":"BANK, EMBEZZLEMENT FROM c. 266 s. 52 ",
            "lastName":"266.52"
            },
            {
            "firstName":"BANK, EMBEZZLEMENT FROM c266 \u00a752",
            "lastName":"266\/52"
            },
            {
            "firstName":"BARBER, UNLICENSED c112 \u00a787R",
            "lastName":"112\/87R\/B"
            },
            {
            "firstName":"BB GUN\/AIR RIFLE, DISCHARGE ON WAY c269 \u00a712B",
            "lastName":"269\/12B\/A"
            },
            {
            "firstName":"BB GUN\/AIR RIFLE, MINOR DISCHARGE c269 \u00a712B",
            "lastName":"269\/12B\/B"
            },
            {
            "firstName":"BB GUN\/AIR RIFLE, MINOR POSSESS c269 \u00a712B",
            "lastName":"269\/12B\/C"
            },
            {
            "firstName":"BB GUN\/AIR RIFLE, SELL\/GIVE TO MINOR c. 269 s. 12A",
            "lastName":"269.12A"
            },
            {
            "firstName":"BB GUN\/AIR RIFLE, SELL\/GIVE TO MINOR c269 \u00a712A",
            "lastName":"269\/12A"
            },
            {
            "firstName":"BESTIALITY c272 \u00a734",
            "lastName":"272\/34\/B"
            },
            {
            "firstName":"BETTING, TAKE\/ALLOW\/PRESENT AT c. 271 s. 17",
            "lastName":"271.17"
            },
            {
            "firstName":"BETTING, TAKE\/ALLOW\/PRESENT AT c271 \u00a717",
            "lastName":"271\/17\/A"
            },
            {
            "firstName":"BETTING, TAKE\/ALLOW\/PRESENT AT,SUBSQ.OFF c271 \u00a717",
            "lastName":"271\/17\/B"
            },
            {
            "firstName":"BICYCLE PATH, DRIVE HORSE\/ANIMAL ON c82 \u00a736",
            "lastName":"82\/36"
            },
            {
            "firstName":"BICYCLE UNREGISTERED\/NO PLATE c85 \u00a711A",
            "lastName":"85\/11A"
            },
            {
            "firstName":"BICYCLE VIOLATION c85 \u00a711B",
            "lastName":"85\/11B"
            },
            {
            "firstName":"BICYCLE VIOLATOR REFUSE IDENTIFY SELF c85 \u00a711C",
            "lastName":"85\/11C"
            },
            {
            "firstName":"BICYCLE, LARCENY OF, SUBSQ.OFF. c266 \u00a741",
            "lastName":"266\/41"
            },
            {
            "firstName":"BILLIARDS\/BOWLING\/AMUSEMENT GAME, UNLIC c140 \u00a7178",
            "lastName":"140\/178"
            },
            {
            "firstName":"BIRD OF PREY, HUNT c131 \u00a775A",
            "lastName":"131\/75A\/B"
            },
            {
            "firstName":"BIRTH CERTIFICATE OF ANOTHER, ATT USE c46 \u00a730",
            "lastName":"46\/30\/A"
            },
            {
            "firstName":"BLASPHEMY c. 272 s. 36",
            "lastName":"272.36"
            },
            {
            "firstName":"BLIND PEDESTRIAN, FAIL STOP FOR * c90 \u00a714A",
            "lastName":"90\/14A\/A"
            },
            {
            "firstName":"BOAT GROUNDED\/ABANDONED c91 \u00a749",
            "lastName":"91\/49"
            },
            {
            "firstName":"BOAT INSURER, FALSE AFFIDAVIT TO c. 266 s. 111",
            "lastName":"266.111"
            },
            {
            "firstName":"BOAT LIFE SAVING DEVICE, NO c90B \u00a75A",
            "lastName":"90B\/5A\/B"
            },
            {
            "firstName":"BOAT OUI LIQUOR OR DRUGS c. 90B s. 8(a)(1)(A)",
            "lastName":"90B.8(a)(1)(A)"
            },
            {
            "firstName":"BOAT OUI LIQUOR OR DRUGS, 4TH OFF. c. 90B s. 8(a)(1)(A)",
            "lastName":"90B.8(a)(1)(A)"
            },
            {
            "firstName":"BOAT OUI\u00bfDRUGS c90B \u00a78(a)",
            "lastName":"90B\/8\/A"
            },
            {
            "firstName":"BOAT OUI\u00bfLIQUOR c90B \u00a78(a)",
            "lastName":"90B\/8\/C"
            },
            {
            "firstName":"BOAT, BUILDING, RAILROAD CAR; LARCENY FROM c. 266 s. 20 ",
            "lastName":"266.2"
            },
            {
            "firstName":"BOAT, LARCENY FROM c266 \u00a720",
            "lastName":"266\/20\/B"
            },
            {
            "firstName":"BOAT, LEAVE SCENE OF PROPERTY DAMAGE BY c90B \u00a78(e)(1)",
            "lastName":"90B\/8\/I"
            },
            {
            "firstName":"BOAT, NEGLIGENT OR RECKLESS OPERATION OF c. 90B s. 8(e)(1)",
            "lastName":"90B.8(e)(1)"
            },
            {
            "firstName":"BOAT, REFUSE STOP\/ID FOR OFFICER c90B \u00a738",
            "lastName":"90B\/38"
            },
            {
            "firstName":"BOAT, TRESPASS ON c102 \u00a71A",
            "lastName":"102\/1A"
            },
            {
            "firstName":"BOAT, UNSAFE OPERATION OF c90B \u00a78(e)(1)",
            "lastName":"90B\/8\/O"
            },
            {
            "firstName":"BOAT\/NON-MOTOR VEH, USE WITHOUT AUTHORITY c266 \u00a763",
            "lastName":"266\/63"
            },
            {
            "firstName":"BODY ARMOR, USE IN FELONY c. 269 s. 10D",
            "lastName":"269.10D"
            },
            {
            "firstName":"BODY ARMOR, USE IN FELONY c269 \u00a710D",
            "lastName":"269\/10D"
            },
            {
            "firstName":"BODY, DISINTER, OR ACCESSORY c. 272 s. 71",
            "lastName":"272.71"
            },
            {
            "firstName":"BODY, IMPROPER DISPOSITION OF HUMAN c. 114 s. 43M",
            "lastName":"114.43M"
            },
            {
            "firstName":"BODY, IMPROPER DISPOSITION OF HUMAN c114  \u00a743M",
            "lastName":"114\/43M"
            },
            {
            "firstName":"BOMB THREAT, FALSE c. 269 s. 14",
            "lastName":"269.14"
            },
            {
            "firstName":"BOMB THREAT, FALSE c269 \u00a714(a)",
            "lastName":"269\/14"
            },
            {
            "firstName":"BOMB\/EXPLOSIVES, POSSESS c. 148 s. 35",
            "lastName":"148.35"
            },
            {
            "firstName":"BOMB\/HIJACK THREAT WITH SERIOUS PUBLIC ALARM c269 \u00a714(c)",
            "lastName":"269\/14\/B"
            },
            {
            "firstName":"BOOKS, FALSIFY\/OMIT ENTRY IN c. 266 s. 67",
            "lastName":"266.67"
            },
            {
            "firstName":"BOOKS, FALSIFY\/OMIT ENTRY IN c266 \u00a767",
            "lastName":"266\/67"
            },
            {
            "firstName":"BOSTON MUNIC CT CLERK FAIL PAY ACCOUNTS c218 \u00a756",
            "lastName":"218\/56"
            },
            {
            "firstName":"BOUNDARY AND MISC. MARKERS, DAMAGE TO c. 266 s. 94",
            "lastName":"266.94"
            },
            {
            "firstName":"BRAKES VIOLATION, MV * c90 \u00a77",
            "lastName":"90\/7\/A"
            },
            {
            "firstName":"BREAK INTO DEPOSITORY c266 \u00a716",
            "lastName":"266\/16\/B"
            },
            {
            "firstName":"BREAK INTO DEPOSITORY, ATTEMPT TO c266 \u00a716",
            "lastName":"266\/16\/C"
            },
            {
            "firstName":"BREAKDOWN LANE VIOLATION * c89 \u00a74B",
            "lastName":"89\/4B\/A"
            },
            {
            "firstName":"BREAKING AND ENTERING",
            "lastName":"21100|"
            },
            {
            "firstName":"BREAKING GLASS IN A BLDG.",
            "lastName":"266\/114"
            },
            {
            "firstName":"BRIBE, BUSINESS c. 271 s. 39(a)",
            "lastName":"271.39(a)"
            },
            {
            "firstName":"BRIDGE, INJURE c266 \u00a7107",
            "lastName":"266\/107\/A"
            },
            {
            "firstName":"BROKER, EMBEZZLEMENT BY c. 266 s. 56 ",
            "lastName":"266.56"
            },
            {
            "firstName":"BROKER, EMBEZZLEMENT BY c266 \u00a756",
            "lastName":"266\/56"
            },
            {
            "firstName":"BROTHEL, DETAIN\/DRUG PERSON IN c272 \u00a713",
            "lastName":"272\/13\/B"
            },
            {
            "firstName":"BROTHEL, DETAIN\/DRUG PERSON IN OR ATTEMPTS c. 272 s. 13",
            "lastName":"272.13"
            },
            {
            "firstName":"BUILDING, DAMAGE TO c. 266 s. 104",
            "lastName":"266.104"
            },
            {
            "firstName":"BUILDING, VANDALIZE c266 \u00a7104",
            "lastName":"266\/104"
            },
            {
            "firstName":"BUILDING, VANDALIZE c266 \u00a794",
            "lastName":"266\/94\/C"
            },
            {
            "firstName":"BURG, UNARM",
            "lastName":"266\/15"
            },
            {
            "firstName":"BURGLARIOUS INSTRUMENT \/ MV MASTER KEY, MAKE OR POSSESS c. 266 s. 49",
            "lastName":"266.49"
            },
            {
            "firstName":"BURGLARIOUS INSTRUMENT, MAKE c266 \u00a749",
            "lastName":"266\/49\/A"
            },
            {
            "firstName":"BURGLARIOUS INSTRUMENT, POSSESS c266 \u00a749",
            "lastName":"266\/49\/B"
            },
            {
            "firstName":"BURGLARY, ARMED & ASSAULT c266 \u00a714",
            "lastName":"266\/14\/C"
            },
            {
            "firstName":"BURGLARY, ARMED c266 \u00a714",
            "lastName":"266\/14\/A"
            },
            {
            "firstName":"BURGLARY, ARMED, SUBSQ.OFF. c266 \u00a714",
            "lastName":"266\/14\/B"
            },
            {
            "firstName":"BURGLARY, FIREARM-ARMED c266 \u00a714",
            "lastName":"266\/14\/G"
            },
            {
            "firstName":"BURGLARY, UNARMED & ASSAULT c266 \u00a714",
            "lastName":"266\/14\/E"
            },
            {
            "firstName":"BURGLARY, UNARMED c. 266 s. 15",
            "lastName":"266.15"
            },
            {
            "firstName":"BURGLARY, UNARMED c266 \u00a715",
            "lastName":"266\/15\/A"
            },
            {
            "firstName":"BURGLARY, UNARMED SUBSQ. OFF. c. 266 s. 15",
            "lastName":"266.15"
            },
            {
            "firstName":"BURGLARY, UNARMED, SUBSQ.OFF. c266 \u00a715",
            "lastName":"266\/15\/B"
            },
            {
            "firstName":"BURGLARY; ARMED, FIREARM c. 266 s. 14",
            "lastName":"266.14"
            },
            {
            "firstName":"BURGLARY; ARMED; ASSAULT ON OCCUPANTS c. 266 s. 14",
            "lastName":"266.14"
            },
            {
            "firstName":"BURN BOAT\/MOTOR VEHICHLE\/PERSONALTY c. 266 s. 5",
            "lastName":"266.5"
            },
            {
            "firstName":"BURN BUILDING c266 \u00a72",
            "lastName":"266\/2\/A"
            },
            {
            "firstName":"BURN BUILDING CONTENTS c266 \u00a72",
            "lastName":"266\/2\/C"
            },
            {
            "firstName":"BURN BUILDING TO DEFRAUD INSURER c266 \u00a710",
            "lastName":"266\/10\/A"
            },
            {
            "firstName":"BURN BUILDING TO DEFRAUD INSURER, ATT c266 \u00a710",
            "lastName":"266\/10\/B"
            },
            {
            "firstName":"BURN BUILDING, ATTEMPT TO c266 \u00a75A",
            "lastName":"266\/5A\/B"
            },
            {
            "firstName":"BURN BUILDING\/CONTENTS c. 266 s. 2",
            "lastName":"266.2"
            },
            {
            "firstName":"BURN BUILDING\/PERSONALY\/M.V. TO DEFRAUD INSURER, OR ATTEMPT TO DO SO c. 266 s. 10",
            "lastName":"266.1"
            },
            {
            "firstName":"BURN LAND\/TREE\/LUMBER\/PRODUCE c266 \u00a75",
            "lastName":"266\/5\/D"
            },
            {
            "firstName":"BURN MOTOR VEHICLE c266 \u00a75",
            "lastName":"266\/5\/C"
            },
            {
            "firstName":"BURN MOTOR VEHICLE, ATTEMPT TO c266 \u00a75A",
            "lastName":"266\/5A\/F"
            },
            {
            "firstName":"BURN MV TO DEFRAUD INSURER c266 \u00a710",
            "lastName":"266\/10\/E"
            },
            {
            "firstName":"BURN MV TO DEFRAUD INSURER, ATTEMPT TO c266 \u00a710",
            "lastName":"266\/10\/F"
            },
            {
            "firstName":"BURN PERSONALTY c266 \u00a75",
            "lastName":"266\/5\/A"
            },
            {
            "firstName":"BURN PERSONALTY, ATTEMPT TO c266 \u00a75A",
            "lastName":"266\/5A\/D"
            },
            {
            "firstName":"BURN PUBLIC BUILDING c266 \u00a72",
            "lastName":"266\/2\/B"
            },
            {
            "firstName":"BURN PUBLIC BUILDING, ATTEMPT TO c266 \u00a75A",
            "lastName":"266\/5A\/C"
            },
            {
            "firstName":"BURN WOODS c. 266 s. 7",
            "lastName":"266.7"
            },
            {
            "firstName":"BURN WOODS c266 \u00a77",
            "lastName":"266\/7"
            },
            {
            "firstName":"BUS DRIVER, ASSAULT c159 \u00a7104",
            "lastName":"159\/104\/A"
            },
            {
            "firstName":"BUS DRIVER, INTERFERE WITH c. 159A s. 31",
            "lastName":"159A.31"
            },
            {
            "firstName":"BUS DRIVER, INTERFERE WITH c159A \u00a731",
            "lastName":"159A\/31"
            },
            {
            "firstName":"BUS, THROW MISSILE AT c159 \u00a7104",
            "lastName":"159\/104\/B"
            },
            {
            "firstName":"BUS\/RAILROAD CAR, THROWING MISSILE OR ASSAULTING c. 159 s. 104",
            "lastName":"159.104"
            },
            {
            "firstName":"BUYING, RECEIVING OR CONCEALING\n                STOLEN GOODS",
            "lastName":"22113|266-60"
            },
            {
            "firstName":"C.O.D. CARRIER, LARCENY OVER $250 BY c. 266 s. 38",
            "lastName":"266.38"
            },
            {
            "firstName":"C.O.D. CARRIER, LARCENY UNDER $250 BY c. 266 s. 38",
            "lastName":"266.38"
            },
            {
            "firstName":"C\/O DISCHARGING OF FIREARMS",
            "lastName":"9.20.010"
            },
            {
            "firstName":"C\/O KNIFE",
            "lastName":"9.20.020"
            },
            {
            "firstName":"C\/O PUBLIC DRINKING",
            "lastName":"9.04.040"
            },
            {
            "firstName":"C\/O RUDE AND  DISORDERLY CONDC",
            "lastName":"9.08.010"
            },
            {
            "firstName":"CABARET ENTERTAINMENT, UNLICENSED c. 140 s. 183C",
            "lastName":"140.183C"
            },
            {
            "firstName":"CABLE TV SERVICE BY FRAUD -$5000, OBTAIN c166 \u00a742A",
            "lastName":"166\/42A\/A"
            },
            {
            "firstName":"CABLE TV\/TELEPHONE SERVICE OVER $5,000 BY FRAUD, OBTAIN OR ATT c. 166 s. 42A",
            "lastName":"166.42A"
            },
            {
            "firstName":"CAMPAIGN EXPENDITURE, +$50 CASH c55 \u00a79",
            "lastName":"55\/9\/B"
            },
            {
            "firstName":"CAMPAIGN EXPENDITURE, IMPROP c55 \u00a77",
            "lastName":"55\/7\/B"
            },
            {
            "firstName":"CARETAKER NEGLECT c265 \u00a713K\/D",
            "lastName":"265\/13K\/D1"
            },
            {
            "firstName":"CARETAKER; PERMITS A&B ON ELDER\/DISABLED PERSON; BODILY INJURY c. 265 s. 13K(d)",
            "lastName":"265.13K(d)"
            },
            {
            "firstName":"CARFENTANYL, TRAFFICKING c94C \u00a732E(c)",
            "lastName":"94C\/32E\/V"
            },
            {
            "firstName":"CARJACKING c. 265 s. 21A",
            "lastName":"265.21A"
            },
            {
            "firstName":"CARJACKING c265 \u00a721A",
            "lastName":"265\/21A\/A"
            },
            {
            "firstName":"CARJACKING, ARMED c. 265 s. 21A",
            "lastName":"265.21A"
            },
            {
            "firstName":"CARJACKING, ARMED c265 \u00a721A",
            "lastName":"265\/21A\/B"
            },
            {
            "firstName":"CARJACKING, ARMED, FIREARM c. 265 s. 21A",
            "lastName":"265.21A"
            },
            {
            "firstName":"CARJACKING, FIREARM-ARMED c265 \u00a721A",
            "lastName":"265\/21A\/C"
            },
            {
            "firstName":"CARRY A FIREARM W\/O LIC.",
            "lastName":"269\/10(A)"
            },
            {
            "firstName":"CARRY DANG WEAP",
            "lastName":"269\/10(B)"
            },
            {
            "firstName":"CARRYING DANGEROUS WEAPON OR KNIFE OVER 4X1 INCHES",
            "lastName":"2CHL9\/B"
            },
            {
            "firstName":"CEMETERY, VANDALIZE c272 \u00a774",
            "lastName":"272\/74"
            },
            {
            "firstName":"CHARITY FUNDRAISING VIOLATION c68 \u00a732(d)",
            "lastName":"68\/32\/A"
            },
            {
            "firstName":"CHECK CASHING VIOLATION c169A \u00a713",
            "lastName":"169A\/13"
            },
            {
            "firstName":"CHECK, FORGERY OF c. 267 s. 1",
            "lastName":"267.1"
            },
            {
            "firstName":"CHEMICAL MACE WITHOUT FID CARD, POSSESS",
            "lastName":"269\/10\/CC"
            },
            {
            "firstName":"CHEMICAL MACE WITHOUT FID CARD, POSSESS c269 \u00a710",
            "lastName":"269\/10\/BB"
            },
            {
            "firstName":"CHILD 5-12 WITHOUT SEAT BELT * c90 \u00a77AA",
            "lastName":"90\/7AA\/B"
            },
            {
            "firstName":"CHILD ABUSE REPORT, IMPROPERLY DISCLOSE c. 119 s. 51E",
            "lastName":"119.51E"
            },
            {
            "firstName":"CHILD ABUSE, MANDATED REPORTER FL REPORT c119 \u00a751A",
            "lastName":"119\/51A\/B"
            },
            {
            "firstName":"CHILD IN NEED OF SERVICES",
            "lastName":"CHIN"
            },
            {
            "firstName":"CHILD IN NEED OF SERVICES (CHINS)",
            "lastName":"12322|119-21"
            },
            {
            "firstName":"CHILD IN NEED OF SERVICES (CHINS)",
            "lastName":"119\/39H"
            },
            {
            "firstName":"CHILD IN NUDE OR SEXUAL ACT, DISTRIB MATERIAL OF c. 272 s. 29B(a)",
            "lastName":"272.29B"
            },
            {
            "firstName":"CHILD IN NUDE OR SEXUAL ACT, LASCIVIOUS POSE\/EXHIBIT c. 272 s. 29A(a)",
            "lastName":"272.29A"
            },
            {
            "firstName":"CHILD IN NUDE, DISTRIB MATERIAL OF c272 \u00a729B(a)",
            "lastName":"272\/29B\/A"
            },
            {
            "firstName":"CHILD IN NUDE, LASCIVIOUS POSE\/EXHIBIT c272 \u00a729A(a)",
            "lastName":"272\/29A\/A"
            },
            {
            "firstName":"CHILD IN SEXUAL ACT, DISTRIB MATERIAL OF c272 \u00a729B(b)",
            "lastName":"272\/29B\/B"
            },
            {
            "firstName":"CHILD IN SEXUAL ACT, POSE\/EXHIBIT c272 \u00a729A(b)",
            "lastName":"272\/29A\/B"
            },
            {
            "firstName":"CHILD LABOR VIOL c149 \u00a778",
            "lastName":"149\/78\/A"
            },
            {
            "firstName":"CHILD PORNOGRAPHY, POSSESS c. 272 s. 29C",
            "lastName":"272.29C"
            },
            {
            "firstName":"CHILD PORNOGRAPHY, POSSESS c272 \u00a729C",
            "lastName":"272\/29C\/A"
            },
            {
            "firstName":"CHILD PORNOGRAPHY, POSSESS, 2ND OFF.  c272 \u00a729C",
            "lastName":"272\/29C\/B"
            },
            {
            "firstName":"CHILD PORNOGRAPHY, POSSESS, 3RD OFF.  c272 \u00a729C",
            "lastName":"272\/29C\/C"
            },
            {
            "firstName":"CHILD PORNOGRAPHY, POSSESS, 3RD OFF. c. 272 s. 29C",
            "lastName":"272.29C"
            },
            {
            "firstName":"CHILD SUPPORT ENFORCEMENT, OBSTRUCT c. 119A s. 2A",
            "lastName":"119A.2A"
            },
            {
            "firstName":"CHILD SUPPORT ENFORCEMENT, OBSTRUCT c119A \u00a72A",
            "lastName":"119A\/2A"
            },
            {
            "firstName":"CHILD UNDER 10, ABANDON c. 119 s. 39",
            "lastName":"119.39"
            },
            {
            "firstName":"CHILD UNDER 10, ABANDON c119 \u00a739",
            "lastName":"119\/39\/A"
            },
            {
            "firstName":"CHILD UNDER 10, ABANDON, WITH DEATH c. 119 s. 39",
            "lastName":"119.39"
            },
            {
            "firstName":"CHILD UNDER 15 BEGGING, EMPLOY\/PERMIT c272 \u00a758",
            "lastName":"272\/58"
            },
            {
            "firstName":"CHILD UNDER 5 WITHOUT CARSEAT * c90 \u00a77AA",
            "lastName":"90\/7AA\/A"
            },
            {
            "firstName":"CHILD, ASSIST ILLEGAL STREET SALES BY c149 \u00a780",
            "lastName":"149\/80"
            },
            {
            "firstName":"CHILD, PERMIT INJURY TO c. 265 s. 13J",
            "lastName":"265.13J"
            },
            {
            "firstName":"CHILD, PERMIT INJURY TO c265 \u00a713J(b)",
            "lastName":"265\/13J\/C"
            },
            {
            "firstName":"CHILD, PERMIT SUBSTANTIAL INJURY TO c. 265 s. 13J",
            "lastName":"265.13J"
            },
            {
            "firstName":"CHILD, PERMIT SUBSTANTIAL INJURY TO c265 \u00a713J(b)",
            "lastName":"265\/13J\/D"
            },
            {
            "firstName":"CHURCH OR SCHOOL, DAMAGE c. 266 s. 98",
            "lastName":"266.98"
            },
            {
            "firstName":"CHURCH, THREAT TO INJURE c. 266 s. 127A",
            "lastName":"266.127A"
            },
            {
            "firstName":"CHURCH, THREAT TO INJURE c266 \u00a7127A",
            "lastName":"266\/127A\/C"
            },
            {
            "firstName":"CHURCH, VANDALIZE c266 \u00a798",
            "lastName":"266\/98\/B"
            },
            {
            "firstName":"CHURCH\/SYNAGOGUE, INJURY OVER $5000 TO c. 266 s. 127A",
            "lastName":"266.127A"
            },
            {
            "firstName":"CHURCH\/SYNAGOGUE, INJURY OVER $5000 TO c266 \u00a7127A",
            "lastName":"266\/127A\/A"
            },
            {
            "firstName":"CHURCH\/SYNAGOGUE, INJURY UNDER $5000 TO c266 \u00a7127A",
            "lastName":"266\/127A\/B"
            },
            {
            "firstName":"CIGARETTE ACQUIRER, UNLICENSED c64C \u00a710 & \u00a72",
            "lastName":"64C\/10\/A"
            },
            {
            "firstName":"CIGARETTE\/MATCH, DROP ON FOREST\/FIELD c. 148 s. 54",
            "lastName":"148.54"
            },
            {
            "firstName":"CIGARETTE\/MATCH, DROP ON FOREST\/FIELD c148 \u00a754",
            "lastName":"148\/54"
            },
            {
            "firstName":"CIGARETTES TO MINOR, DELIVER c270 \u00a76",
            "lastName":"270\/6\/A"
            },
            {
            "firstName":"CIGARETTES WITHOUT MFR'S ADDRESSEE LABEL c64C \u00a710",
            "lastName":"64C\/10\/F"
            },
            {
            "firstName":"CIGARETTES-TO-MINORS WARNING, FAIL POST c270 \u00a77",
            "lastName":"270\/7\/A"
            },
            {
            "firstName":"CIGARETTES, FAIL DISPLAY LICENSE TO SELL c64C \u00a72",
            "lastName":"64C\/2"
            },
            {
            "firstName":"CIGARETTES, IMPORT FOR UNLICENSED BUYER c64C \u00a710",
            "lastName":"64C\/10\/H"
            },
            {
            "firstName":"CIGARETTES, OBTAIN FROM UNLIC SOURCE c64C \u00a710",
            "lastName":"64C\/10\/I"
            },
            {
            "firstName":"CIGARETTES, POSSESS -12000 UNSTAMPED c64C \u00a735",
            "lastName":"64C\/35\/B"
            },
            {
            "firstName":"CIGARETTES, SELL -12000 UNSTAMPED c. 64C s. 34",
            "lastName":"64C.34"
            },
            {
            "firstName":"CIGARETTES, SELL -12000 UNSTAMPED c64C \u00a734",
            "lastName":"64C\/34\/B"
            },
            {
            "firstName":"CIGARETTES, SELL +12000 UNSTAMPED c64C \u00a734",
            "lastName":"64C\/34\/A"
            },
            {
            "firstName":"CIGARETTES, SELL SINGLE UNPACKAGED c94 \u00a7307A",
            "lastName":"94\/307A"
            },
            {
            "firstName":"CIGARETTES, SELL WITHOUT LICENSE c64C \u00a710 & \u00a72",
            "lastName":"64C\/10\/J"
            },
            {
            "firstName":"CITATION, ATTEMPT TO FALSIFY c. 90C s. 10",
            "lastName":"90C.10"
            },
            {
            "firstName":"CIVIL RIGHTS ORDER VIOLATION c12 \u00a711J",
            "lastName":"12\/11J\/A"
            },
            {
            "firstName":"CIVIL RIGHTS VIOL. NO BO INJ",
            "lastName":"265\/37"
            },
            {
            "firstName":"CIVIL RIGHTS VIOLATION c265 \u00a737",
            "lastName":"265\/37\/A"
            },
            {
            "firstName":"CIVIL RIGHTS VIOLATION OR ATTEMPT c. 265 s. 37",
            "lastName":"265.37"
            },
            {
            "firstName":"CIVIL RIGHTS VIOLATION WITH BODILY INJURY OR ATTEMPT c. 265 s. 37",
            "lastName":"265.37"
            },
            {
            "firstName":"CIVIL RIGHTS VIOLATION WITH INJURY c265 \u00a737",
            "lastName":"265\/37\/B"
            },
            {
            "firstName":"CIVIL RIGHTS VIOLATION WITH INJURY, ATT c265 \u00a737",
            "lastName":"265\/37\/D"
            },
            {
            "firstName":"CIVIL RIGHTS VIOLATION, ATTEMPTED c265 \u00a737",
            "lastName":"265\/37\/C"
            },
            {
            "firstName":"CLASS A, MAN, DISTR, DISP",
            "lastName":"94C\/32"
            },
            {
            "firstName":"COCAINE (c.94C s. 31 Class B(a)(4)), DISTRIBUTE OR POSSESS WITH INTENT c. 94C s. 32A(c)",
            "lastName":"94C.32A(c)"
            },
            {
            "firstName":"COCAINE (c.94C s. 31 Class B(a)(4)), DISTRIBUTE OR POSSESS WITH INTENT, SUBSQ. OFF. c. 94C s. 32A(d)",
            "lastName":"94C.32A(d)"
            },
            {
            "firstName":"COCAINE (c.94C s. 31(a)(4)), DISTRIBUTE OR POSSESS WITH INTENT, TO MINOR c. 94C s. 32F(d)",
            "lastName":"94C.32F(d)"
            },
            {
            "firstName":"COCAINE (c.94C s. 31(a)(4)), TRAFFICK IN c. 94C s. 32E(b)(2) - 28 to 100 g",
            "lastName":"94C.32E(b)(2)"
            },
            {
            "firstName":"COCAINE (c.94C s. 31(a)(4)), TRAFFICK IN c. 94C s. 32E(b)(3) - 100 to 200 g",
            "lastName":"94C.32E(b)(3)"
            },
            {
            "firstName":"COCAINE (c.94C s. 31(a)(4)), TRAFFICK IN c. 94C s. 32E(b)(4) - 200 or more g",
            "lastName":"94C.32E(b)(4)"
            },
            {
            "firstName":"COCAINE (c.94C s. 31(a)(4)), TRAFFICKING IN c. 94C s. 32E(b)(1) - 14 to 28 g",
            "lastName":"94C.32E(b)(1)"
            },
            {
            "firstName":"COCAINE, DISTRIBUTE c94C \u00a732A(c)",
            "lastName":"94C\/32A\/A"
            },
            {
            "firstName":"COCAINE, DISTRIBUTE TO MINOR c94C \u00a732F(d)",
            "lastName":"94C\/32F\/A"
            },
            {
            "firstName":"COCAINE, DISTRIBUTE, SUBSQ.OFF. c94C \u00a732A(d)",
            "lastName":"94C\/32A\/B"
            },
            {
            "firstName":"COCAINE, POSSESS TO DISTRIBUTE c94C \u00a732A(c)",
            "lastName":"94C\/32A\/C"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN c94C \u00a732E(b)",
            "lastName":"94C\/32E\/A"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, OVER 100 GRAMS c94C \u00a732E(b)(3)",
            "lastName":"94C\/32E\/A2"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, OVER 14 GRAMS c94C \u00a732E(b)(1)",
            "lastName":"94C\/32E\/A1"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, OVER 18 GRAMS, LESS 36 c94C \u00a732E(b)",
            "lastName":"94C\/32E\/A00"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, OVER 200 GRAMS     c94C \u00a732E(b)(4)",
            "lastName":"94C\/32E\/A22"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, OVER 28  GRAMS c94C \u00a732E(b)(2)",
            "lastName":"94C\/32E\/A11"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, OVER 36 GRAMS, LESS 100 c94C \u00a732E(b)",
            "lastName":"94C\/32E\/B0"
            },
            {
            "firstName":"COCAINE, TRAFFICKING IN, SUBSEQUENT OFFENSE c94C \u00a732E(b)",
            "lastName":"94C\/32E\/A0"
            },
            {
            "firstName":"COLLEGE ENDORSEMENT, FALSE CLAIM OF c. 266 s. 90",
            "lastName":"266.9"
            },
            {
            "firstName":"COMMERCIAL COMPUTER SERVICES, FRAUD c. 266 s. 33A",
            "lastName":"266.33A"
            },
            {
            "firstName":"COMMERCIAL DUMPSTER, USE OF ANOTHER'S c. 266 s. 146",
            "lastName":"c. 266 s. 146"
            },
            {
            "firstName":"COMMON CARRIER W\/O LOCAL AGENT, FOREIGN c159 \u00a77",
            "lastName":"159\/7"
            },
            {
            "firstName":"COMMON CARRIER, LARCENY FROM c. 266 s. 30",
            "lastName":"266.3"
            },
            {
            "firstName":"COMMON CARRIER, LARCENY FROM c266 \u00a730(1)",
            "lastName":"266\/30\/F"
            },
            {
            "firstName":"COMMON CARRIER, LARCENY FROM, SUBSQ. OFF. c. 266 s. 30",
            "lastName":"266.3"
            },
            {
            "firstName":"COMMON CARRIER'S GROSS NEGLIGENCE c265 \u00a730",
            "lastName":"265\/30"
            },
            {
            "firstName":"COMMON NIGHTWALKER THIRD CONVICTION c. 272 s. 62",
            "lastName":"272.62"
            },
            {
            "firstName":"COMPOUND\/CONCEAL FELONY c. 268 s. 36",
            "lastName":"268.36"
            },
            {
            "firstName":"COMPUTER SVCE, ATT FALSELY OBTAIN COMMER c266 \u00a733A",
            "lastName":"266\/33A\/A"
            },
            {
            "firstName":"COMPUTER SYSTEM, UNAUTHORIZED ACCESS TO c266 \u00a7120F",
            "lastName":"266\/120F"
            },
            {
            "firstName":"CONFINE OR PUT IN FEAR TO STEAL\/OR ATTEMPT c. 265 s. 21",
            "lastName":"265.21"
            },
            {
            "firstName":"CONSIGNEE\/FACTOR, CONVERSION BY c266 \u00a788",
            "lastName":"266\/88"
            },
            {
            "firstName":"CONSP VIOL. CNTRLLD SUB LAWS",
            "lastName":"94\/40"
            },
            {
            "firstName":"CONSPIRACY c. 274 s. 7 cl. (1) - Death or Life",
            "lastName":"274.7 cl. (1)"
            },
            {
            "firstName":"CONSPIRACY c. 274 s. 7 cl. (2) - Felony exceeding 10 years up to life",
            "lastName":"274.7 cl. (2)"
            },
            {
            "firstName":"CONSPIRACY c. 274 s. 7 cl. (3) - Felony not more than 10 years",
            "lastName":"274.7 cl. (3)"
            },
            {
            "firstName":"CONSPIRACY c. 274 s. 7 cl. (4) - Other Crime",
            "lastName":"274.7 cl. (4)"
            },
            {
            "firstName":"CONSPIRACY c274 \u00a77",
            "lastName":"274\/7"
            },
            {
            "firstName":"CONSPIRACY TO VIOLATE DRUG LAW c. 94C s. 40",
            "lastName":"94C.40"
            },
            {
            "firstName":"CONSPIRACY TO VIOLATE DRUG LAW c94C \u00a740",
            "lastName":"94C\/40"
            },
            {
            "firstName":"CONSUMER CREDIT COST DISCLOSURE VIOL c140D \u00a731",
            "lastName":"140D\/31"
            },
            {
            "firstName":"CONTEMPT IN SUPPLEMENTARY PROCESS c224 \u00a718",
            "lastName":"224\/18"
            },
            {
            "firstName":"CONTEMPT, CRIMINAL (Common Law)",
            "lastName":"COMLAW2"
            },
            {
            "firstName":"CONTRIBUTE TO DELINQUENCY OF CHILD c. 119 s. 63",
            "lastName":"119.63"
            },
            {
            "firstName":"CONTRIBUTE TO DELINQUENCY OF CHILD c119 \u00a763",
            "lastName":"119\/63"
            },
            {
            "firstName":"CORI, DISSEMINATE\/SEEK UNLAWFULLY c6 \u00a7178",
            "lastName":"6\/178\/A"
            },
            {
            "firstName":"CORI, DISSEMINATE\/SEEK UNLAWFULLY,FALSIFY c. 6 s. 178",
            "lastName":"6.178"
            },
            {
            "firstName":"CORPORATE CREDIT\/MONEY\/PROPERTY, MISUSE c. 266 s. 74",
            "lastName":"266.74"
            },
            {
            "firstName":"CORPORATE CREDIT\/MONEY\/PROPERTY, MISUSE c266 \u00a774",
            "lastName":"266\/74"
            },
            {
            "firstName":"CORPORATE REPORT, FAIL FILE c156 \u00a750",
            "lastName":"156\/50"
            },
            {
            "firstName":"CORPORATE STATEMENT, FALSE c155 \u00a74",
            "lastName":"155\/48"
            },
            {
            "firstName":"CORRECTIONAL INSTITUTION, DISTURB c. 268 s. 30",
            "lastName":"268.3"
            },
            {
            "firstName":"CORRECTIONAL INSTITUTION, DISTURB c268 \u00a730",
            "lastName":"268\/30"
            },
            {
            "firstName":"COUNTERFEIT COIN c267 \u00a717",
            "lastName":"267\/17\/A"
            },
            {
            "firstName":"COUNTERFEIT COINS, POSSESS 10 c267 \u00a717",
            "lastName":"267\/17\/B"
            },
            {
            "firstName":"COUNTERFEIT DRUG, DISTRIBUTE c94C \u00a732G",
            "lastName":"94C\/32G\/A"
            },
            {
            "firstName":"COUNTERFEIT DRUG, DISTRIBUTE OR POSSESS WITH INTENT c. 94C s. 32G",
            "lastName":"94C.32G"
            },
            {
            "firstName":"COUNTERFEIT DRUG, POSSESS TO DISTRIBUTE c94C \u00a732G",
            "lastName":"94C\/32G\/B"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIB 1000+\/$10000+ c266 \u00a7147(b)(3)",
            "lastName":"266\/147\/E"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIB 101-999\/$1001-$9999 c266 \u00a7147(b)(2)",
            "lastName":"266\/147\/C"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE c. 266 s. 147(b)(1)",
            "lastName":"266.147(b)(1)"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE c266 \u00a7147(b)(1)",
            "lastName":"266\/147\/A"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE, 1000+\/$10,000+ c. 266 s. 147(b)(3)",
            "lastName":"266.147(b)(3)"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE, 101-999\/$1,001-$9999 c. 266 s. 147(b)(2)",
            "lastName":"266.147(b)(2)"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE, 2ND OFF. c. 266 s. 147(b)(2)",
            "lastName":"266.147(b)(2)"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE, 2ND OFF. c266 \u00a7147(b)(2)",
            "lastName":"266\/147\/B"
            },
            {
            "firstName":"COUNTERFEIT MARK, DISTRIBUTE, 3RD OFF. c266 \u00a7147(b)(3)",
            "lastName":"266\/147\/D"
            },
            {
            "firstName":"COUNTERFEIT NOTE OR TRAVELLER'S CHECK, POSSESS c. 267 s. 12",
            "lastName":"267.12"
            },
            {
            "firstName":"COUNTERFEIT NOTE, POSSESS c267 \u00a712",
            "lastName":"267\/12\/A"
            },
            {
            "firstName":"COUNTERFEIT NOTES, COMMON UTTERER OF c. 267 s. 11",
            "lastName":"267.11"
            },
            {
            "firstName":"COUNTERFEIT NOTES, COMMON UTTERER OF c267 \u00a711",
            "lastName":"267\/11"
            },
            {
            "firstName":"COUNTERFEIT NOTES, POSSESS 10 c. 267 s. 9",
            "lastName":"267.9"
            },
            {
            "firstName":"COUNTERFEIT NOTES, POSSESS 10 c267 \u00a79",
            "lastName":"267\/9"
            },
            {
            "firstName":"COUNTERFEIT TRAVELLER'S CHECK, POSSESS c267 \u00a712",
            "lastName":"267\/12\/B"
            },
            {
            "firstName":"COUNTERFEITING EQUIPMENT, MANUFACTURE c267 \u00a713",
            "lastName":"267\/13\/A"
            },
            {
            "firstName":"COUNTERFEITING EQUIPMENT, MANUFACTURE OR POSSESS c. 267 s. 13",
            "lastName":"267.13"
            },
            {
            "firstName":"COUNTERFEITING EQUIPMENT, POSSESS c267 \u00a713",
            "lastName":"267\/13\/B"
            },
            {
            "firstName":"COUNTY BUILDING, VANDALIZE c266 \u00a797",
            "lastName":"266\/97"
            },
            {
            "firstName":"COURT PROCEEDINGS, DISRUPT c. 268 s. 13C",
            "lastName":"268.13C"
            },
            {
            "firstName":"COURT PROCEEDINGS, DISRUPT c268 \u00a713C",
            "lastName":"268\/13C"
            },
            {
            "firstName":"COURT\/JUDGE\/JUROR, PICKETING c268 \u00a713A",
            "lastName":"268\/13A"
            },
            {
            "firstName":"CREDIT +$250 BY FALSE FINANCIAL STATEMNT c. 266 s. 33(2)",
            "lastName":"266.33(2)"
            },
            {
            "firstName":"CREDIT +$250 BY FALSE FINANCIAL STATEMNT c266 \u00a733(2) & \u00a730(1)",
            "lastName":"266\/33\/C"
            },
            {
            "firstName":"CREDIT CARD FRAUD OVER $1200 BY MERCHANT c266 \u00a737C(g)",
            "lastName":"266\/37C\/B"
            },
            {
            "firstName":"CREDIT CARD FRAUD OVER $1200 c266 \u00a737C(e)",
            "lastName":"266\/37C\/A"
            },
            {
            "firstName":"CREDIT CARD FRAUD OVER $250 BY MERCHANT c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD FRAUD OVER $250 BY MERCHANT c266 \u00a737C(g)",
            "lastName":"266\/37C\/B"
            },
            {
            "firstName":"CREDIT CARD FRAUD OVER $250 c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD FRAUD OVER $250 c266 \u00a737C(e)",
            "lastName":"266\/37C\/A"
            },
            {
            "firstName":"CREDIT CARD FRAUD UNDER $1200 BY MERCHANT c266 \u00a737B(i)",
            "lastName":"266\/37B\/B"
            },
            {
            "firstName":"CREDIT CARD FRAUD UNDER $1200 c266 \u00a737B(g)",
            "lastName":"266\/37B\/A1"
            },
            {
            "firstName":"CREDIT CARD FRAUD UNDER $250 BY MERCHANT c266 \u00a737B(i)",
            "lastName":"266\/37B\/B"
            },
            {
            "firstName":"CREDIT CARD FRAUD UNDER $250 c266 \u00a737B(g)",
            "lastName":"266\/37B\/A"
            },
            {
            "firstName":"CREDIT CARD, ALLOW IMPROP USE UNDER $1200 c266 \u00a737B(h)",
            "lastName":"266\/37B\/C"
            },
            {
            "firstName":"CREDIT CARD, ALLOW IMPROP USE UNDER $250 c266 \u00a737B(h)",
            "lastName":"266\/37B\/C"
            },
            {
            "firstName":"CREDIT CARD, FALSE REPORT OF LOST c266 \u00a737B(k)",
            "lastName":"266\/37B\/D"
            },
            {
            "firstName":"CREDIT CARD, FALSE STATEMENT TO OBTAIN c266 \u00a737B(a)",
            "lastName":"266\/37B\/E"
            },
            {
            "firstName":"CREDIT CARD, FORGE OR UTTER FORGED c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD, FORGE OR UTTER FORGED c266 \u00a737C(c)",
            "lastName":"266\/37C\/C"
            },
            {
            "firstName":"CREDIT CARD, IMPROPER USE OVER $1200 c266 \u00a737C(d)",
            "lastName":"266\/37C\/D"
            },
            {
            "firstName":"CREDIT CARD, IMPROPER USE OVER $250 c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD, IMPROPER USE OVER $250 c266 \u00a737C(d)",
            "lastName":"266\/37C\/D"
            },
            {
            "firstName":"CREDIT CARD, IMPROPER USE UNDER $1200  c266 \u00a737B(f)",
            "lastName":"266\/37B\/F"
            },
            {
            "firstName":"CREDIT CARD, IMPROPER USE UNDER $250  c266 \u00a737B(f)",
            "lastName":"266\/37B\/F"
            },
            {
            "firstName":"CREDIT CARD, LARCENY OF c266 \u00a737B(b)",
            "lastName":"266\/37B\/G"
            },
            {
            "firstName":"CREDIT CARD, NON-CARDHOLDER SIGN c266 \u00a737B(e)",
            "lastName":"266\/37B\/H"
            },
            {
            "firstName":"CREDIT CARD, POSSESS BLANK c266 \u00a737C(i)",
            "lastName":"266\/37C\/E"
            },
            {
            "firstName":"CREDIT CARD, POSSESS COUNTERFEIT PRESS c266 \u00a737C(j)",
            "lastName":"266\/37C\/F"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE IMPROP OVER $1200 c266 \u00a737C(h)",
            "lastName":"266\/37C\/G"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE IMPROP OVER $250 c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE IMPROP OVER $250 c266 \u00a737C(h)",
            "lastName":"266\/37C\/G"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE IMPROP UNDER $250 c266 \u00a737B(j)",
            "lastName":"266\/37B\/I"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE IMPROPER c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE IMPROPER c266 \u00a737C(b)",
            "lastName":"266\/37C\/H"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE LOST c266 \u00a737B(c)",
            "lastName":"266\/37B\/J"
            },
            {
            "firstName":"CREDIT CARD, RECEIVE STOLEN c266 \u00a737B(b)",
            "lastName":"266\/37B\/K"
            },
            {
            "firstName":"CREDIT CARD, SELL\/BUY c266 \u00a737B(d)",
            "lastName":"266\/37B\/L"
            },
            {
            "firstName":"CREDIT CARD, TAKE AS SECURITY c. 266 s. 37C ",
            "lastName":"266.37C"
            },
            {
            "firstName":"CREDIT CARD, VIOLATIONS c. 266 s. 37B",
            "lastName":"266.37B"
            },
            {
            "firstName":"CREDIT REPORT OBTAINED BY FALSE PRETENSE c93 \u00a766",
            "lastName":"93\/66"
            },
            {
            "firstName":"CRIME REPORT, FALSE c. 269 s. 13A",
            "lastName":"269.13A"
            },
            {
            "firstName":"CRIME REPORT, FALSE c269 \u00a713A",
            "lastName":"269\/13A"
            },
            {
            "firstName":"CRIMINAL INQUIRY ONLY",
            "lastName":"81111|"
            },
            {
            "firstName":"CRIMINAL PROCEEDING, WITHHOLD EVIDENCE FROM c268 \u00a713E",
            "lastName":"268\/13E\/A"
            },
            {
            "firstName":"CROSSWALK VIOLATION * c89 \u00a711",
            "lastName":"89\/11"
            },
            {
            "firstName":"CRUELTY-NEGLECT OF CHILDREN",
            "lastName":"12317|"
            },
            {
            "firstName":"CURFEW VIOLATION",
            "lastName":"C\/O 9.16.0"
            },
            {
            "firstName":"CURFEW VIOLATION",
            "lastName":"2CHL18"
            },
            {
            "firstName":"CURFEW, VIOLATE c. 40 s. 37A",
            "lastName":"40.37A"
            },
            {
            "firstName":"DANGEROUS WEAPON ON SCHOOL GROUNDS,CARRY c269 \u00a710(j)",
            "lastName":"269\/10\/A"
            },
            {
            "firstName":"DANGEROUS WEAPON OR FIREARM ON SCHOOL GROUNDS,CARRY c. 269 s. 10(j)",
            "lastName":"269.10(j)"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY c. 269 s. 10(b)",
            "lastName":"269.10(b)"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY c269 \u00a710(b)",
            "lastName":"269\/10\/B"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY MISD c269 \u00a710(b)",
            "lastName":"269\/10\/WW"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY, 2ND OFF. c. 269 s. 10(d)",
            "lastName":"269.10(d)"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY, 2ND OFF. c269 \u00a710(b) & (d)",
            "lastName":"269\/10\/C"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY, 3RD OFF. c. 269 s. 10(d)",
            "lastName":"269.10(d)"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY, 3RD OFF. c269 \u00a710(b) & (d)",
            "lastName":"269\/10\/D"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY, 4TH OFF. c269 \u00a710(b) & (d)",
            "lastName":"269\/10\/E"
            },
            {
            "firstName":"DANGEROUS WEAPON, CARRY, NO PRIOR FELONIES c. 269 s. 10(b)",
            "lastName":"269.10(b)"
            },
            {
            "firstName":"DANGEROUS WEAPONS UNLAWFULLY CARRIED",
            "lastName":"12212|269-10 (A)"
            },
            {
            "firstName":"DANGEROUS WEAPONS, MFR\/SELL CERTAIN c. 269 s. 12",
            "lastName":"269.12"
            },
            {
            "firstName":"DANGEROUS WEAPONS, MFR\/SELL CERTAIN c269 \u00a712",
            "lastName":"269\/12"
            },
            {
            "firstName":"DAY CARE, UNLICENSED c28A \u00a711(a)",
            "lastName":"28A\/11\/B"
            },
            {
            "firstName":"DEATH CERTIFICATE, FILE FALSE c46 \u00a714",
            "lastName":"46\/14\/B"
            },
            {
            "firstName":"DEATH, FAIL REPORT c46 \u00a78",
            "lastName":"46\/8\/C"
            },
            {
            "firstName":"DEER TAGGING VIOLATION c131 \u00a772",
            "lastName":"131\/72\/B"
            },
            {
            "firstName":"DEFACE PROPERTY c266 \u00a7126",
            "lastName":"266\/126"
            },
            {
            "firstName":"DEFACEMENT OF REAL OR PERSONAL PROPERTY c. 266 s. 126A",
            "lastName":"266.126A"
            },
            {
            "firstName":"DEFAULT WARRANT 0501CR4400 A&B DANGEROUS WEAPON",
            "lastName":"FDEFAULT"
            },
            {
            "firstName":"DEFECTIVE EQUIPMENT, OPERATING WITH c. 90 s. 1",
            "lastName":"90.1"
            },
            {
            "firstName":"DEFRAUDING, POSE AS ANOTHER W\/O EXPRESS AUTHORIZATION c. 266 s. 37E",
            "lastName":"266. 37E"
            },
            {
            "firstName":"DEGREE, FALSE CLAIM TO HOLD SCHOOL c266 \u00a789",
            "lastName":"266\/89\/A"
            },
            {
            "firstName":"DEPT OF PUB UTILS, FALSE STATEMENT TO c268 \u00a76",
            "lastName":"268\/6\/A"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY -$1200, MALICIOUS c266 \u00a7127",
            "lastName":"266\/127\/C"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY -$1200, WANTON c266 \u00a7127",
            "lastName":"266\/127\/D"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY -$250, MALICIOUS c266 \u00a7127",
            "lastName":"266\/127\/C"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY -$250, WANTON c266 \u00a7127",
            "lastName":"266\/127\/D"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY -$250, WANTON OR MALICIOUS c. 266 s. 127",
            "lastName":"266.127"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY +$1200, MALICIOUS c266 \u00a7127",
            "lastName":"266\/127\/A"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY +$1200, WANTON c266 \u00a7127",
            "lastName":"266\/127\/B"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY +$250, MALICIOUS c. 266 s. 127",
            "lastName":"266.127"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY +$250, MALICIOUS c266 \u00a7127",
            "lastName":"266\/127\/A"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY +$250, WANTON c. 266 s. 127",
            "lastName":"266.127"
            },
            {
            "firstName":"DESTRUCTION OF PROPERTY +$250, WANTON c266 \u00a7127",
            "lastName":"266\/127\/B"
            },
            {
            "firstName":"DESTRUCTION OR INJURY OF PERSONAL PROPERTY",
            "lastName":"22212|266-127"
            },
            {
            "firstName":"DISGUISE TO OBSTRUCT JUSTICE c. 268 s. 34",
            "lastName":"268.34"
            },
            {
            "firstName":"DISGUISE TO OBSTRUCT JUSTICE c268 \u00a734",
            "lastName":"268\/34"
            },
            {
            "firstName":"DISORDERLY CONDUCT AT POLL c56 \u00a746",
            "lastName":"56\/46"
            },
            {
            "firstName":"DISORDERLY CONDUCT c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"DISORDERLY CONDUCT c272 \u00a753",
            "lastName":"272\/53\/F"
            },
            {
            "firstName":"DISORDERLY CONDUCT ON PUB CONVEY,3RD AND SUBSQ. OFF c. 272 s. 43",
            "lastName":"272.43"
            },
            {
            "firstName":"DISORDERLY CONDUCT ON PUB CONVEY,3RD OFF c272 \u00a743",
            "lastName":"272\/43\/B"
            },
            {
            "firstName":"DISORDERLY CONDUCT ON PUBLIC CONVEYANCE c. 272 s. 43",
            "lastName":"272.43"
            },
            {
            "firstName":"DISORDERLY CONDUCT ON PUBLIC CONVEYANCE c272 \u00a743",
            "lastName":"272\/43\/A"
            },
            {
            "firstName":"DISORDERLY CONDUCT, SUBSQ. OFF. c272 \u00a753",
            "lastName":"272\/53\/J"
            },
            {
            "firstName":"DISORDERLY HOUSE, KEEP c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"DISORDERLY PERSON",
            "lastName":"272\/53"
            },
            {
            "firstName":"DISPOSAL OF RUBBISH c. 270 s. 16",
            "lastName":"270 .16"
            },
            {
            "firstName":"DIST OF SCHOOL OR ASSEMBLY",
            "lastName":"272\/40"
            },
            {
            "firstName":"DISTRIBUTION OF CLASS B, DRUGS",
            "lastName":"41221|94C-32A"
            },
            {
            "firstName":"DISTRIBUTION OF CLASS B, DRUGS\n                WITHIN 1000&APOS; SCHOOL ZONE",
            "lastName":"41218|94C-32J"
            },
            {
            "firstName":"DISTRIBUTION OR POSSESSION W\/I TO DISTRIBUTE",
            "lastName":"41200|"
            },
            {
            "firstName":"DISTRIBUTION OXYCODENE c94C \u00a732A(a)",
            "lastName":"94C\/32A\/R"
            },
            {
            "firstName":"DISTURBING A PUBLIC ASSEMBLY",
            "lastName":"12415|272-53"
            },
            {
            "firstName":"DISTURBING THE PEACE c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"DISTURBING THE PEACE c272 \u00a753",
            "lastName":"272\/53\/G"
            },
            {
            "firstName":"DISTURBING THE PEACE WHILE ARMED",
            "lastName":"269\/10 (B)"
            },
            {
            "firstName":"DISTURBING THE PEACE, SUBSQ. OFF. c272 \u00a753",
            "lastName":"272\/53\/K"
            },
            {
            "firstName":"DIVORCE, ISSUE UNLAWFUL CERTIFICATE OF c208 \u00a744",
            "lastName":"208\/44"
            },
            {
            "firstName":"DNA DATABASE SAMPLE, REFUSE PROVIDE c22E \u00a711",
            "lastName":"22E\/11"
            },
            {
            "firstName":"DNA SAMPLE, REFUSE TO PROVIDE c. 22E s. 11",
            "lastName":"22E.11"
            },
            {
            "firstName":"DOG KENNEL, UNLICENSED c140 \u00a7137A",
            "lastName":"140\/137A\/A"
            },
            {
            "firstName":"DOG ORDER, DISOBEY c140 \u00a7157",
            "lastName":"140\/157\/A"
            },
            {
            "firstName":"DOG ORDINANCE\/BY-LAW VIOLATION c140 \u00a7173",
            "lastName":"140\/173"
            },
            {
            "firstName":"DOG UNLEASHED AT REST AREA c140 \u00a7174B",
            "lastName":"140\/174B"
            },
            {
            "firstName":"DOG, FAIL LICENSE c140 \u00a7137",
            "lastName":"140\/137\/A"
            },
            {
            "firstName":"DOG, FAIL MUZZLE\/RESTRAIN c140 \u00a7168",
            "lastName":"140\/168"
            },
            {
            "firstName":"DOG, TETHERING OR CONFINING VIOLATION c140 \u00a7174E(f)",
            "lastName":"140\/174E"
            },
            {
            "firstName":"DOG\/CAT RABIES VACCINATION VIOLATION c140 \u00a7145B",
            "lastName":"140\/145B"
            },
            {
            "firstName":"DOG\/CAT, MOTORIST FL REPORT INJURY TO * c272 \u00a780H",
            "lastName":"272\/80H"
            },
            {
            "firstName":"DRINKING ALCOHOLIC BEVERAGES IN PUBLIC",
            "lastName":"51311|16-5.1"
            },
            {
            "firstName":"DRINKING IN PUBLIC c. 138 s. 1",
            "lastName":"138. 1"
            },
            {
            "firstName":"DRINKING\/POSSESS ALCOHOL PRIVATE PROP WO CONSENT",
            "lastName":"2CHL1\/AA"
            },
            {
            "firstName":"DRINKING\/POSSING OPEN ALCOHOLIC BEVERAGE IN PUBLIC",
            "lastName":"2CHL1\/A"
            },
            {
            "firstName":"DRUG DEALER FAIL PAY TAX c64K \u00a79",
            "lastName":"64K\/9"
            },
            {
            "firstName":"DRUG FUNDS, INDUCE MINOR TO POSSESS c. 94C s. 32K",
            "lastName":"94C.32K"
            },
            {
            "firstName":"DRUG FUNDS, INDUCE MINOR TO POSSESS c94C \u00a732K",
            "lastName":"94C\/32K\/A"
            },
            {
            "firstName":"DRUG LABEL, REMOVE\/ALTER c94C \u00a725(4)",
            "lastName":"94C\/25\/C"
            },
            {
            "firstName":"DRUG PARAPHERNALIA, DISTRIBUTE c94C \u00a732I(a)",
            "lastName":"94C\/32I\/A"
            },
            {
            "firstName":"DRUG PARAPHERNALIA, DISTRIBUTE OR POSSESS WITH INTENT c. 94C s. 32I(a)",
            "lastName":"94C.32I(a)"
            },
            {
            "firstName":"DRUG PARAPHERNALIA, POSSESS TO DISTRIB c94C \u00a732I(a)",
            "lastName":"94C\/32I\/B"
            },
            {
            "firstName":"DRUG PARAPHERNALIA, SELL TO MINOR c. 94C s. 32I(b)",
            "lastName":"94C.32I(b)"
            },
            {
            "firstName":"DRUG PARAPHERNALIA, SELL TO MINOR c94C \u00a732I(b)",
            "lastName":"94C\/32I\/C"
            },
            {
            "firstName":"DRUG TO CONFINE c265 \u00a726B",
            "lastName":"265\/26B\/A"
            },
            {
            "firstName":"DRUG VIOLATION NEAR SCHOOL c. 94C s. 32J",
            "lastName":"94C.32J"
            },
            {
            "firstName":"DRUG VIOLATION NEAR SCHOOL\/PARK c. 94C s. 32J",
            "lastName":"94C.32J"
            },
            {
            "firstName":"DRUG VIOLATION NEAR SCHOOL\/PARK c94C \u00a732J",
            "lastName":"94C\/32J"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS A c94C \u00a732(a)",
            "lastName":"94C\/32\/A"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS A, SUBSQ.OFF. c94C \u00a732(b)",
            "lastName":"94C\/32\/B"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS B c94C \u00a732A(a)",
            "lastName":"94C\/32A\/E"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS B, SUBSQ.OFF. c94C \u00a732A(b)",
            "lastName":"94C\/32A\/F"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS C c94C \u00a732B(a)",
            "lastName":"94C\/32B\/A"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS C, SUBSQ.OFF. c94C \u00a732B(b)",
            "lastName":"94C\/32B\/B"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS D c94C \u00a732C(a)",
            "lastName":"94C\/32C\/A"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS D, SUBSQ.OFF. c94C \u00a732C(b)",
            "lastName":"94C\/32C\/B"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS E c94C \u00a732D(a)",
            "lastName":"94C\/32D\/A"
            },
            {
            "firstName":"DRUG, DISTRIBUTE CLASS E, SUBSQ.OFF. c94C \u00a732D(b)",
            "lastName":"94C\/32D\/B"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT CLASS C c. 94C s. 32B(a)",
            "lastName":"94C.32B(a)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT CLASS C, SUBSQ. OFF. c. 94C s. 32B(b)",
            "lastName":"94C.32B(b)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT CLASS D c. 94C s. 32C(a)",
            "lastName":"94C.32C(a)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT CLASS D, SUBSQ. OFF. c. 94C s. 32C(b)",
            "lastName":"94C.32C(b)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT CLASS E c. 94C s. 32D(a)",
            "lastName":"94C.32D(a)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT CLASS E, SUBSQ. OFF. c. 94C s. 32D(b)",
            "lastName":"94C.32D(b)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT TO MINOR CLASS A c. 94C s. 32F(a)",
            "lastName":"94C.32F(a)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT TO MINOR CLASS B c. 94C s. 32F(b)",
            "lastName":"94C.32F(b)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT TO MINOR CLASS C c. 94C s. 32F(c)",
            "lastName":"94C.32F(c)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT, CLASS A c. 94C s. 32(a)",
            "lastName":"94C.32(a)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT, CLASS A, SUBSQ. OFF. c. 94C s. 32(b)",
            "lastName":"94C.32(b)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT, CLASS B c. 94C s. 32A(a)",
            "lastName":"94C.32A(a)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE OR POSSESS WITH INTENT, CLASS B, SUBSQ. OFF. c. 94C s. 32A(b)",
            "lastName":"94C.32A(b)"
            },
            {
            "firstName":"DRUG, DISTRIBUTE TO MINOR CLASS B c94C \u00a732F(b)",
            "lastName":"94C\/32F\/C"
            },
            {
            "firstName":"DRUG, DISTRIBUTE TO MINOR CLASS C c94C \u00a732F(c)",
            "lastName":"94C\/32F\/D"
            },
            {
            "firstName":"DRUG, FAIL REPORT DISPENSING c94C \u00a724(a)",
            "lastName":"94C\/24\/A"
            },
            {
            "firstName":"DRUG, FAIL REPORT DISPENSING, SUBSQ.OFF. c94C \u00a724(a)",
            "lastName":"94C\/24\/B"
            },
            {
            "firstName":"DRUG, FALSE REGIS NUMBER FOR c. 94C s. 33(a)",
            "lastName":"94C.33(a)"
            },
            {
            "firstName":"DRUG, FALSE REGIS NUMBER FOR c94C \u00a733(a)",
            "lastName":"94C\/33\/A"
            },
            {
            "firstName":"DRUG, FALSE REGIS NUMBER FOR, SUBSQ.OFF. c94C \u00a733(c)",
            "lastName":"94C\/33\/B"
            },
            {
            "firstName":"DRUG, INDUCE MINOR TO DISTRIBUTE c. 94C s. 32K",
            "lastName":"94C.32K"
            },
            {
            "firstName":"DRUG, INDUCE MINOR TO DISTRIBUTE c94C \u00a732K",
            "lastName":"94C\/32K\/B"
            },
            {
            "firstName":"DRUG, LARCENY OF c94C \u00a737",
            "lastName":"94C\/37"
            },
            {
            "firstName":"DRUG, OBTAIN BY FRAUD c. 94C s. 33(b)",
            "lastName":"94C.33(b)"
            },
            {
            "firstName":"DRUG, OBTAIN BY FRAUD c94C \u00a733(b)",
            "lastName":"94C\/33\/C"
            },
            {
            "firstName":"DRUG, OBTAIN BY FRAUD, SUBSQ.OFF. c94C \u00a733(c)",
            "lastName":"94C\/33\/D"
            },
            {
            "firstName":"DRUG, PHARMACIST FAIL LABEL c94C \u00a721",
            "lastName":"94C\/21\/A"
            },
            {
            "firstName":"DRUG, PHARMACIST FAIL LABEL, SUBSQ. OFF. c. 94C s. 21",
            "lastName":"94C.21"
            },
            {
            "firstName":"DRUG, POSSESS CLASS A c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS A c94C \u00a734",
            "lastName":"94C\/34\/A"
            },
            {
            "firstName":"DRUG, POSSESS CLASS A, SUBSQ. OFF. c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS A, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/B"
            },
            {
            "firstName":"DRUG, POSSESS CLASS B c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS B c94C \u00a734",
            "lastName":"94C\/34\/C"
            },
            {
            "firstName":"DRUG, POSSESS CLASS B, SUBSQ. OFF. c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS B, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/D"
            },
            {
            "firstName":"DRUG, POSSESS CLASS C c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS C c94C \u00a734",
            "lastName":"94C\/34\/E"
            },
            {
            "firstName":"DRUG, POSSESS CLASS C, SUBSQ. OFF. c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS C, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/F"
            },
            {
            "firstName":"DRUG, POSSESS CLASS D c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS D c94C \u00a734",
            "lastName":"94C\/34\/G"
            },
            {
            "firstName":"DRUG, POSSESS CLASS D, SUBSQ. OFF. c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS D, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/H"
            },
            {
            "firstName":"DRUG, POSSESS CLASS E c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"DRUG, POSSESS CLASS E c94C \u00a734",
            "lastName":"94C\/34\/I"
            },
            {
            "firstName":"DRUG, POSSESS CLASS E, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/N"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTR TO MINOR CLASS A c94C \u00a732F(a)",
            "lastName":"94C\/32F\/E"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTR TO MINOR CLASS B c94C \u00a732F(b)",
            "lastName":"94C\/32F\/F"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS A c94C \u00a732(a)",
            "lastName":"94C\/32\/C"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS A, SUBSQ. c94C \u00a732(b)",
            "lastName":"94C\/32\/D"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS B c94C \u00a732A(a)",
            "lastName":"94C\/32A\/G"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS B, SUBSQ. c94C \u00a732A(b)",
            "lastName":"94C\/32A\/H"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS C c94C \u00a732B(a)",
            "lastName":"94C\/32B\/C"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS C, SUBSQ. c94C \u00a732B(b)",
            "lastName":"94C\/32B\/D"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS D c94C \u00a732C(a)",
            "lastName":"94C\/32C\/C"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS D, SUBSQ. c94C \u00a732C(b)",
            "lastName":"94C\/32C\/D"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS E c94C \u00a732D(a)",
            "lastName":"94C\/32D\/C"
            },
            {
            "firstName":"DRUG, POSSESS TO DISTRIB CLASS E, SUBSQ. c94C \u00a732D(b)",
            "lastName":"94C\/32D\/D"
            },
            {
            "firstName":"DRUG,LARCENYOF c. 94C s. 37",
            "lastName":"94C.37"
            },
            {
            "firstName":"DSCHG WEAP\/HUNT NR HGWY\/DWEL",
            "lastName":"131\/58"
            },
            {
            "firstName":"DUMPSTER, USE OF ANOTHER'S COMMERCIAL c266 \u00a7146",
            "lastName":"266\/146"
            },
            {
            "firstName":"ELDER ABUSE, FAIL REPORT c19A \u00a715(a)",
            "lastName":"19A\/15"
            },
            {
            "firstName":"ELDER\/DISABLED, PERMIT INJURY TO c265 \u00a713K(d)",
            "lastName":"265\/13K\/C"
            },
            {
            "firstName":"ELDER\/DISABLED, PERMIT SERIOUS INJURY TO c265 \u00a713K(e)",
            "lastName":"265\/13K\/D"
            },
            {
            "firstName":"ELECTRIC STUN GUN, SELL\/POSSESS c. 140 s. 131J",
            "lastName":"140.131J"
            },
            {
            "firstName":"ELECTRIC STUN GUN, SELL\/POSSESS c141 \u00a731J",
            "lastName":"140\/131J"
            },
            {
            "firstName":"ELECTRICIAN, UNLICENSED c141 \u00a75",
            "lastName":"141\/5\/A"
            },
            {
            "firstName":"ELECTRICIAN, UNLICENSED, SUBSQ. OFF. c. 141 s. 5",
            "lastName":"141.5"
            },
            {
            "firstName":"ELECTRICITY, FRAUDULENT USE OF c164 \u00a7127",
            "lastName":"164\/127"
            },
            {
            "firstName":"ELECTRONIC MESSAGING WHILE OPERATING MV",
            "lastName":"90\/13B"
            },
            {
            "firstName":"ELEVATOR REPAIR PERSON, UNLICENSED c143 \u00a771D",
            "lastName":"143\/71D"
            },
            {
            "firstName":"EMERGENCY MEDICAL TECHNICIAN,IMPERSONATE c111C \u00a712",
            "lastName":"111C\/12\/C"
            },
            {
            "firstName":"EMERGENCY VEHICLE, OBSTRUCT * c89 \u00a77A",
            "lastName":"89\/7A"
            },
            {
            "firstName":"EMERGENCY VEHICLE, WILFULLY OBSTRUCT c89 \u00a77",
            "lastName":"89\/7"
            },
            {
            "firstName":"EMERGENCY VEHICLE, WILFULLY OBSTRUCT, 2D c89 \u00a77",
            "lastName":"89\/7\/B"
            },
            {
            "firstName":"EMERGENCY VEHICLE, WILFULLY OBSTRUCT, 3D c89 \u00a77",
            "lastName":"89\/7\/C"
            },
            {
            "firstName":"EMISSIONS CONTROL TAMPER OR FALSIFY c. 111 s. 142M",
            "lastName":"111.142M"
            },
            {
            "firstName":"EMISSIONS, ATT REGISTER MV WITH IMPROPER c90 \u00a72",
            "lastName":"90\/2\/E"
            },
            {
            "firstName":"EMISSIONS, REGISTER MV WITH IMPROPER c90 \u00a72",
            "lastName":"90\/2\/D"
            },
            {
            "firstName":"EMISSIONS, REGISTER MV WITH IMPROPER OR ATTEMPTS c. 90 s. 2",
            "lastName":"90.2"
            },
            {
            "firstName":"EMISSIONS\/SAFETY INSPECTION, UNLICENSED c. 90 s. 7W",
            "lastName":"90.7W"
            },
            {
            "firstName":"EMPLOYER FAIL ALLOW EMPLOYEE DAY OF REST c149 \u00a748",
            "lastName":"149\/48"
            },
            {
            "firstName":"EMPLOYER FAIL GIVE PAY STUB c149 \u00a7148",
            "lastName":"149\/148\/A"
            },
            {
            "firstName":"EMPLOYER FAIL PAY WAGES TIMELY c149 \u00a7148",
            "lastName":"149\/148\/B"
            },
            {
            "firstName":"EMPLOYER WAGE VIOLATION c. 149 s. 148",
            "lastName":"149.148"
            },
            {
            "firstName":"EMPLOYER WILFULLY FAIL GIVE PAY STUB, SUBSQ. c149 \u00a7148",
            "lastName":"149\/148\/E"
            },
            {
            "firstName":"EMPLOYER WILFULLY FAIL PAY WAGES TIMELY c149 \u00a7148",
            "lastName":"149\/148\/G"
            },
            {
            "firstName":"ENDANGERMENT TO CHILDREN, RECKLESS c. 265 s. 13L",
            "lastName":"265 . 13L"
            },
            {
            "firstName":"ENT W\/O BRK INT TO COM. FEL",
            "lastName":"266\/17"
            },
            {
            "firstName":"ENTER AT NIGHT FOR FELONY, ARMED, PERSON IN FEAR c266 \u00a717",
            "lastName":"266\/17\/C"
            },
            {
            "firstName":"ENTER AT NIGHT FOR FELONY,PERSON IN FEAR c266 \u00a717",
            "lastName":"266\/17\/A"
            },
            {
            "firstName":"ENTER DWELLING AT NIGHT FOR FELONY c. 266 s. 18",
            "lastName":"266.18"
            },
            {
            "firstName":"ENTER DWELLING AT NIGHT FOR FELONY c266 \u00a718",
            "lastName":"266\/18\/A"
            },
            {
            "firstName":"ENTER DWELLING AT NIGHT FOR FELONY, ARMED c266 \u00a718",
            "lastName":"266\/18\/C"
            },
            {
            "firstName":"ENTER DWELLING AT NIGHT, ARMED, FIREARM, FOR FELONY c. 266 s. 18",
            "lastName":"266.18"
            },
            {
            "firstName":"ENTER DWELLING FOR FELONY BY FALSE PRETENSES c266 \u00a718A",
            "lastName":"266\/18A"
            },
            {
            "firstName":"ENTER W\/LARCENY OR W\/I FELONY BY FALSE PRETENSES c. 266 s. 18A",
            "lastName":"266.18A"
            },
            {
            "firstName":"ENTERTAINER FAIL FILE STAGE-NAME CERTIFc140 \u00a7181A",
            "lastName":"140\/181A"
            },
            {
            "firstName":"ENTERTAINMENT, UNLICENSED c140 \u00a7182",
            "lastName":"140\/182\/A"
            },
            {
            "firstName":"ENTICEMENT OF CHILDREN",
            "lastName":"265\/26C"
            },
            {
            "firstName":"EQUIPMENT VIOLATION, MISCELLANEOUS MV * c90 \u00a77",
            "lastName":"90\/7\/D"
            },
            {
            "firstName":"ESCAPE FROM COUNTY WORK RELEASE PROGRAM c. 127 s. 49",
            "lastName":"127.49"
            },
            {
            "firstName":"ESCAPE FROM COUNTY WORK RELEASE PROGRAM c127 \u00a749",
            "lastName":"127\/49\/A"
            },
            {
            "firstName":"ESCAPE FROM MUNICIPAL LOCKUP c. 268 s. 15A",
            "lastName":"268.15A"
            },
            {
            "firstName":"ESCAPE FROM MUNICIPAL LOCKUP c268 \u00a715A",
            "lastName":"268\/15A"
            },
            {
            "firstName":"ESCAPE FROM OFFICER, AID c. 268 s. 17",
            "lastName":"268.17"
            },
            {
            "firstName":"ESCAPE FROM OFFICER, AID c268 \u00a717",
            "lastName":"268\/17"
            },
            {
            "firstName":"ESCAPE FROM PENAL INSTITUTION, PERMIT c. 268 s. 19",
            "lastName":"268.19"
            },
            {
            "firstName":"ESCAPE FROM PENAL INSTITUTION\/COURT c268 \u00a716",
            "lastName":"268\/16\/A"
            },
            {
            "firstName":"ESCAPE FROM PENAL INSTITUTION\/COURT, ATT c268 \u00a716",
            "lastName":"268\/16\/B"
            },
            {
            "firstName":"ESCAPE FROM PENAL INSTITUTION\/COURT\/SDP CENTER OR ATTEMPTS c. 268 s. 16",
            "lastName":"268.16"
            },
            {
            "firstName":"ESCAPE FROM POLICE OFFICER (Common Law)",
            "lastName":"COMLAW3"
            },
            {
            "firstName":"ESCAPE FROM S.D.P. TREATMENT CENTER c268 \u00a716",
            "lastName":"268\/16\/C"
            },
            {
            "firstName":"ESCAPE FROM STATE WORK RELEASE PROGRAM c. 127 s. 49",
            "lastName":"127.49"
            },
            {
            "firstName":"ESCAPE FROM STATE WORK RELEASE PROGRAM c127 \u00a749",
            "lastName":"127\/49\/B"
            },
            {
            "firstName":"ESCAPE OR AID ESCAPE FROM DYS c120 \u00a726",
            "lastName":"120\/26"
            },
            {
            "firstName":"ESCAPE, AID ACCUSED MISDEMEANANT TO c268 \u00a715",
            "lastName":"268\/15\/C"
            },
            {
            "firstName":"ESCAPE, AID CONVICT TO c268 \u00a715",
            "lastName":"268\/15\/B"
            },
            {
            "firstName":"ESCAPE, AID FELON (STATE PRISON) OR ACCUSED FELON TO c. 268 s. 15",
            "lastName":"268.15"
            },
            {
            "firstName":"ESCAPE, AID FELON OR ACCUSED FELON TO c268 \u00a715",
            "lastName":"268\/15\/A"
            },
            {
            "firstName":"ESCAPE, AID MISDEMEANANT OR HC FELON CONVICT TO c. 268 s. 15",
            "lastName":"268.15"
            },
            {
            "firstName":"ESCAPE, NEGLIGENTLY PERMIT PRISONER TO c268 \u00a720",
            "lastName":"268\/20\/A"
            },
            {
            "firstName":"ESCAPE, VOLUNTARILY PERMIT PRISONER TO c268 \u00a718",
            "lastName":"268\/18"
            },
            {
            "firstName":"EXCAVATION BY-LAW VIOLATION c40 \u00a721(19)",
            "lastName":"40\/21\/A"
            },
            {
            "firstName":"EXPLOSION, MALICIOUS c266 \u00a7101",
            "lastName":"266\/101"
            },
            {
            "firstName":"EXPLOSIVES, POSSESS TO INJURE c266 \u00a7102",
            "lastName":"266\/102\/B"
            },
            {
            "firstName":"EXPLOSIVES, THROW\/PLACE\/EXPLODE c266 \u00a7102",
            "lastName":"266\/102\/A"
            },
            {
            "firstName":"EXPLOSIVES, THROW\/PLACE\/EXPLODE OR POSSESS TO INJURE c. 266 s. 102",
            "lastName":"266.102"
            },
            {
            "firstName":"EXTORTION BY FALSE REPORT OF CRIME c. 265 s. 25",
            "lastName":"EXTORTION BY FALSE REPORT"
            },
            {
            "firstName":"EXTORTION BY FALSE REPORT OF CRIME c265 \u00a725",
            "lastName":"265\/25\/A"
            },
            {
            "firstName":"EXTORTION BY POLICE OFFICER c265 \u00a725",
            "lastName":"265\/25\/C"
            },
            {
            "firstName":"EXTORTION BY THREAT OF INJURY c265 \u00a725",
            "lastName":"265\/25\/B"
            },
            {
            "firstName":"EXTORTION OR ATTEMPTS c. 265 s. 25",
            "lastName":"265.25"
            },
            {
            "firstName":"FAIL TO STOP FOR POLICE-MV",
            "lastName":"90\/25"
            },
            {
            "firstName":"FAILURE \/ REFUSAL TO REMOVE TRASH",
            "lastName":"51411|16-5.1"
            },
            {
            "firstName":"FAILURE TO DELIVER CERTIFICATE OF TITLE OR SALVAGE TITLE TO TRANSFEREE OR REGISTRAR c. 90D s. 32(b)",
            "lastName":"90D.32(b)"
            },
            {
            "firstName":"FAILURE TO OBEY PAVEMENT MARKINGS\/LINES, OPERATING AND c. 89 s. 4",
            "lastName":"89.4"
            },
            {
            "firstName":"FAILURE TO REG.,SEX OFFENDER",
            "lastName":"6\/178H"
            },
            {
            "firstName":"FAILURE TO REGISTER - SEX OFFENDER REGISTRY",
            "lastName":"11412|"
            },
            {
            "firstName":"FAILURE TO REGISTER OR VERIFY REGISRATION INFO BY SEX OFFENDER c. 6 s. 178H",
            "lastName":"6.178H"
            },
            {
            "firstName":"FAILURE TO REGISTER OR VERIFY REGISRATION INFO BY SEX OFFENDER, SUBSQ. OFF. c. 6 s. 178H",
            "lastName":"6.178H"
            },
            {
            "firstName":"FAILURE TO STOP FOR POLICE c.90 s. 25",
            "lastName":"c. 90 s. 25"
            },
            {
            "firstName":"FAILURE TO YIELD RIGHT OF WAY TO FIRE ENGINE, PATROL VEHICLE, OR AMBULANCE c. 89 s. 7",
            "lastName":"89.7"
            },
            {
            "firstName":"FAILURE TO YIELD RIGHT OF WAY TO FIRE ENGINE, PATROL VEHICLE, OR AMBULANCE, SUBSQ. OFF. c. 89 s. 7",
            "lastName":"89.7"
            },
            {
            "firstName":"FALSE ALARM FROM POLICE CALL BOX c268 \u00a732",
            "lastName":"268\/32\/A"
            },
            {
            "firstName":"FALSE ALARM FROM POLICE CALL BOX OR TAMPER WITH POLICE\/FIRE CALL BOX c. 268 s. 32",
            "lastName":"268.32"
            },
            {
            "firstName":"FALSE CLAIM TO GOVERNMENT AGENCY c. 266 s. 67B",
            "lastName":"266.67B"
            },
            {
            "firstName":"FALSE CLAIM TO GOVERNMENT AGENCY c266 \u00a767B",
            "lastName":"266\/67B"
            },
            {
            "firstName":"FALSE NAME, GIVING TO AN OFFICER WHEN ARRESTED",
            "lastName":"268. 34A"
            },
            {
            "firstName":"FALSE NAME\/SSN, ARRESTEE FURNISH c268 \u00a734A",
            "lastName":"268\/34A"
            },
            {
            "firstName":"FALSE OR SILENT 911 CALL, MAKING c269 \u00a714B",
            "lastName":"269\/14B\/A"
            },
            {
            "firstName":"FALSE PRETENSE IN COMMER TRANSACTN -$250 c. 266 s. 33(1)",
            "lastName":"266.33(1)"
            },
            {
            "firstName":"FALSE PRETENSE IN COMMER TRANSACTN -$250 c266 \u00a733(1) & \u00a730(1)",
            "lastName":"266\/33\/B"
            },
            {
            "firstName":"FALSE PRETENSE IN COMMER TRANSACTN +$250 c. 266 s. 33(1)",
            "lastName":"266.33(1)"
            },
            {
            "firstName":"FALSE PRETENSE IN COMMER TRANSACTN +$250 c266 \u00a733(1) & \u00a730(1)",
            "lastName":"266\/33\/A"
            },
            {
            "firstName":"FALSE PRETENSE OF TRADE, OBTAIN GOODS BY c. 266 s. 73",
            "lastName":"266.73"
            },
            {
            "firstName":"FALSE PRETENSE OF TRADE, OBTAIN GOODS BY c266 \u00a773",
            "lastName":"266\/73"
            },
            {
            "firstName":"FALSE STATEMENT UNDER PENALTY OF PERJURY c. 268 s. 1A",
            "lastName":"268.1A"
            },
            {
            "firstName":"FALSE STATEMENT UNDER PENALTY OF PERJURY c268 \u00a71A",
            "lastName":"268\/1A"
            },
            {
            "firstName":"FARE EVASION, MBTA c. 159 s. 101",
            "lastName":"159.101"
            },
            {
            "firstName":"FELONY FOR HIRE c. 265 s. 13G",
            "lastName":"265.13G"
            },
            {
            "firstName":"FENCE, VANDALIZE c266 \u00a7114",
            "lastName":"266\/114\/B"
            },
            {
            "firstName":"FENTANYL, TRAFFICKING IN, OVER 10 GRAMS c94C \u00a732E(c)",
            "lastName":"94C\/32E\/Q"
            },
            {
            "firstName":"FENTANYL, TRAFFICKING IN, OVER 200 GRAMS c94C \u00a732E(c)",
            "lastName":"94C\/32E\/Q1"
            },
            {
            "firstName":"FIDUCIARY, EMBEZZLEMENT\/MISAPPLICATN BY c266 \u00a757",
            "lastName":"266\/57"
            },
            {
            "firstName":"FIGHT BY ARRANGEMENT, AID\/PROMOTE c. 265 s. 10",
            "lastName":"265.1"
            },
            {
            "firstName":"FIGHT BY ARRANGEMENT, AID\/PROMOTE c265 \u00a710",
            "lastName":"265\/10"
            },
            {
            "firstName":"FILING FALSE DOCUMENT WITH REGISTRAR OF DEEDS c266 \u00a735\/A(b)4",
            "lastName":"266\/35\/A\/B4"
            },
            {
            "firstName":"FINANCIAL STATEMENT, PUBLISH FALSE c266 \u00a792",
            "lastName":"266\/92"
            },
            {
            "firstName":"FIRE ALARM, DISABLE c. 266 s. 11",
            "lastName":"266.11"
            },
            {
            "firstName":"FIRE ALARM, DISABLE c266 \u00a711",
            "lastName":"266\/11"
            },
            {
            "firstName":"FIRE ALARM, FALSE c. 269 s. 13",
            "lastName":"269.13"
            },
            {
            "firstName":"FIRE ALARM, FALSE c269 \u00a713",
            "lastName":"269\/13"
            },
            {
            "firstName":"FIRE CALL BOX, TAMPER WITH c268 \u00a732",
            "lastName":"268\/32\/B"
            },
            {
            "firstName":"FIRE DOORS LOCKED DURING BUSINESS HOURS c149 \u00a7126",
            "lastName":"149\/126"
            },
            {
            "firstName":"FIRE IN OPEN, SET c48 \u00a713",
            "lastName":"48\/13"
            },
            {
            "firstName":"FIRE ON ANOTHER'S LAND, SET c266 \u00a78",
            "lastName":"266\/8\/A"
            },
            {
            "firstName":"FIRE ON ANOTHER'S LAND, SET c266 \u00a79",
            "lastName":"266\/9\/B"
            },
            {
            "firstName":"FIRE ON LAND, SET c. 266 s. 8",
            "lastName":"266.8"
            },
            {
            "firstName":"FIRE PREVENTION ORDER, DISOBEY c148 \u00a75",
            "lastName":"148\/5"
            },
            {
            "firstName":"FIRE PREVENTION REGULATIONS VIOLATION c148 \u00a710B",
            "lastName":"148\/10B"
            },
            {
            "firstName":"FIRE RULE\/REGULATION\/ORDER VIOLATION c148 \u00a730",
            "lastName":"148\/30"
            },
            {
            "firstName":"FIRE VIOLATION, MISCELLANEOUS c148 \u00a734",
            "lastName":"148\/34"
            },
            {
            "firstName":"FIRE, HOTEL MANAGER FAIL RESPOND TO c266 \u00a713A",
            "lastName":"266\/13A"
            },
            {
            "firstName":"FIRE, LARCENY AT c. 266 s. 23",
            "lastName":"266.23"
            },
            {
            "firstName":"FIREARM APPLIC, FALSE STATEMENT ON c. 140 s. 129",
            "lastName":"140.129"
            },
            {
            "firstName":"FIREARM APPLIC, FALSE STATEMENT ON, SUBSQ c. 140 s. 129",
            "lastName":"140.129"
            },
            {
            "firstName":"FIREARM ID CARD APPLIC, FALSE STATEMENT ON c. 140 s. 129B(8)",
            "lastName":"140.129B(8)"
            },
            {
            "firstName":"FIREARM ID CARD APPLIC, FALSE STATEMENT ON c140 \u00a7129B(8)",
            "lastName":"140\/129B"
            },
            {
            "firstName":"FIREARM IN FELONY, POSSESS c. 265 s. 18B",
            "lastName":"265.18B"
            },
            {
            "firstName":"FIREARM IN FELONY, POSSESS c265 \u00a718",
            "lastName":"265\/18B\/A"
            },
            {
            "firstName":"FIREARM IN FELONY, POSSESS LGE CAPACITY c265 \u00a718B",
            "lastName":"265\/18B\/C"
            },
            {
            "firstName":"FIREARM IN FELONY, POSSESS LGE CAPACITY, SUBSQ. c265 \u00a718B",
            "lastName":"265\/18B\/D"
            },
            {
            "firstName":"FIREARM IN FELONY, POSSESS, SUBSQ.OFF c265 \u00a718",
            "lastName":"265\/18B\/B"
            },
            {
            "firstName":"FIREARM IN VEHICLE, LEAVE c140 \u00a7131C",
            "lastName":"140\/131C"
            },
            {
            "firstName":"FIREARM LICENSE APPLIC, FALSE c140 \u00a7131(h)",
            "lastName":"140\/131\/A"
            },
            {
            "firstName":"FIREARM LICENSE RESTRICTION VIOL c140 \u00a7131(a) or (b)",
            "lastName":"140\/131\/C"
            },
            {
            "firstName":"FIREARM LICENSE VIOLATION c. 140 s. 131(h)",
            "lastName":"140.131(h)"
            },
            {
            "firstName":"FIREARM LICENSE, IMPROP ISSUE c140 \u00a7131(k)",
            "lastName":"140\/131\/B"
            },
            {
            "firstName":"FIREARM LICENSE\/ID CARD, FALSE c. 140 s. 131I",
            "lastName":"140.131I"
            },
            {
            "firstName":"FIREARM ON SCHOOL GROUNDS, CARRY c269 \u00a710(j)",
            "lastName":"269\/10\/F"
            },
            {
            "firstName":"FIREARM ON WAY, CARRY LOADED LARGE CAPACITY c. 269 s. 12D(a)",
            "lastName":"269.12D(a)"
            },
            {
            "firstName":"FIREARM ON WAY, CARRY LOADED LARGE CAPACITY c269 \u00a712D(a)",
            "lastName":"269\/12D\/C"
            },
            {
            "firstName":"FIREARM ON WAY, CARRY UNLOADED LARGE CAPACITY c269 \u00a712D(b)",
            "lastName":"269\/12D\/D"
            },
            {
            "firstName":"FIREARM ON WAY, CARRY UNLOADED LARGE CAPACITYc. 269 s. 12D(b)",
            "lastName":"269.12D(b)"
            },
            {
            "firstName":"FIREARM PERMIT, IMPROP ISSUE c140 \u00a7131A",
            "lastName":"140\/131A"
            },
            {
            "firstName":"FIREARM POSSESS LARGE CAPACITY c. 269 s. 10(m)",
            "lastName":"269.10(m)"
            },
            {
            "firstName":"FIREARM POSSESS LARGE CAPACITY, WITH VALID FID c. 269 s. 10(m)",
            "lastName":"269.10(m)"
            },
            {
            "firstName":"FIREARM PURCHASE FOR ANOTHER c140 \u00a7131E",
            "lastName":"140\/131E"
            },
            {
            "firstName":"FIREARM SALE TO MINOR\/ALIEN  c. 140 s. 130",
            "lastName":"140.13"
            },
            {
            "firstName":"FIREARM SALE TO MINOR\/ALIEN c140 \u00a7130",
            "lastName":"140\/130"
            },
            {
            "firstName":"FIREARM SALE, IMPROPER c140 \u00a7128",
            "lastName":"140\/128\/A"
            },
            {
            "firstName":"FIREARM SALE, UNLICENSED c140 \u00a7128",
            "lastName":"140\/128\/C"
            },
            {
            "firstName":"FIREARM SALE, VIOLATION c. 140 s. 128",
            "lastName":"140.128"
            },
            {
            "firstName":"FIREARM SERIAL NO., DEFACE c269 \u00a711C",
            "lastName":"269\/11C\/A"
            },
            {
            "firstName":"FIREARM SERIAL NO., DEFACE OR RECEIVE W\/DEFACED NO. c. 269 s. 11C",
            "lastName":"269.11C"
            },
            {
            "firstName":"FIREARM SURRENDER ORDER, VIOLATE c. 209A s. 3C",
            "lastName":"209A.3C"
            },
            {
            "firstName":"FIREARM SURRENDER ORDER, VIOLATE c209A \u00a73C",
            "lastName":"209A\/3C"
            },
            {
            "firstName":"FIREARM TO MINOR, SELL\/TRANSFER LARGE CAPACITY c269 \u00a710F(b)",
            "lastName":"269\/10F\/B"
            },
            {
            "firstName":"FIREARM TRANSFER\/LOSS, OWNER FL REPORT c140 \u00a7129C",
            "lastName":"140\/129C\/A"
            },
            {
            "firstName":"FIREARM UNATTENDED c269 \u00a710",
            "lastName":"269\/10\/DD"
            },
            {
            "firstName":"FIREARM VIOL WITH 1 PRIOR VIOLENT\/DRUG CRIME c269 \u00a710G(a)",
            "lastName":"269\/10G\/A"
            },
            {
            "firstName":"FIREARM VIOL WITH 2 PRIOR VIOLENT\/DRUG CRIMES c269 \u00a710G(b)",
            "lastName":"269\/10G\/B"
            },
            {
            "firstName":"FIREARM VIOL WITH 3 PRIOR VIOLENT\/DRUG CRIMES c269 \u00a710G(c)",
            "lastName":"269\/10G\/C"
            },
            {
            "firstName":"FIREARM W\/DEFACED NO., POSSESS c269 \u00a711C",
            "lastName":"269\/11C\/C"
            },
            {
            "firstName":"FIREARM W\/DEFACED NO., POSSESS IN FELONY c. 269 s. 11B",
            "lastName":"269.11B"
            },
            {
            "firstName":"FIREARM W\/DEFACED NO., POSSESS IN FELONY c269 \u00a711B",
            "lastName":"269\/11B"
            },
            {
            "firstName":"FIREARM W\/DEFACED NO., RECEIVE c269 \u00a711C",
            "lastName":"269\/11C\/B"
            },
            {
            "firstName":"FIREARM W\/I 500' OF DWELLING\/DISCHARGE HWAY c. 131 s. 58",
            "lastName":"131.58"
            },
            {
            "firstName":"FIREARM W\/O FID CARD, POSSESS c. 269 s. 10(h)",
            "lastName":"269.10(h)"
            },
            {
            "firstName":"FIREARM W\/O FID CARD, SUBSQ. OFF. c. 269 s. 10(h)",
            "lastName":"269.10(h)"
            },
            {
            "firstName":"FIREARM WITHIN 500 FT OF DWELLING c131 \u00a758",
            "lastName":"131\/58\/D"
            },
            {
            "firstName":"FIREARM WITHOUT FID CARD, POSSESS c269 \u00a710(h)",
            "lastName":"269\/10\/G"
            },
            {
            "firstName":"FIREARM WITHOUT FID CARD, SUBSQ.OFF. c269 \u00a710(h)",
            "lastName":"269\/10\/H"
            },
            {
            "firstName":"FIREARM, ALIEN POSSESS c. 140 s. 131H",
            "lastName":"140.131H"
            },
            {
            "firstName":"FIREARM, ALIEN POSSESS c140 \u00a7131H",
            "lastName":"140\/131H"
            },
            {
            "firstName":"FIREARM, CARRY W\/ AMMUNITION c. 269 s. 10(n)",
            "lastName":"269.10(n)"
            },
            {
            "firstName":"FIREARM, CARRY W\/O LICENSE c. 269 s. 10(a)",
            "lastName":"269.10(a)"
            },
            {
            "firstName":"FIREARM, CARRY W\/O LICENSE, 2ND OFF. c. 269 s. 10(d)",
            "lastName":"269.10(d)"
            },
            {
            "firstName":"FIREARM, CARRY W\/O LICENSE, 3RD OFF. c. 269 s. 10(d)",
            "lastName":"269.10(d)"
            },
            {
            "firstName":"FIREARM, CARRY W\/O LICENSE, 4TH OFF. c. 269 s. 10(d)",
            "lastName":"269.10(d)"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE c269 \u00a710(a)",
            "lastName":"269\/10\/J"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE LOADED, 2ND OFF. c269 \u00a710",
            "lastName":"269\/10\/HH"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE LOADED, 3RD OFF. c269 \u00a710",
            "lastName":"269\/10\/JJ"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE LOADED, 4TH OFF. c269 \u00a710",
            "lastName":"269\/10\/KK"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE, 2ND OFF. c269 \u00a710(a) & (d)",
            "lastName":"269\/10\/K"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE, 3RD OFF. c269 \u00a710(a) & (d)",
            "lastName":"269\/10\/L"
            },
            {
            "firstName":"FIREARM, CARRY WITHOUT LICENSE, 4TH OFF. c269 \u00a710(a) & (d)",
            "lastName":"269\/10\/M"
            },
            {
            "firstName":"FIREARM, CARRYING LOADED c269 \u00a710EE",
            "lastName":"269\/10\/EE"
            },
            {
            "firstName":"FIREARM, DISCHARGE NEAR HWAY c131 \u00a758",
            "lastName":"131\/58\/B"
            },
            {
            "firstName":"FIREARM, DISCHARGE WITHIN 500 FT OF BLDG c. 269 s. 12E",
            "lastName":"269.12E"
            },
            {
            "firstName":"FIREARM, DISCHARGE WITHIN 500 FT OF BLDG c269 \u00a712E",
            "lastName":"269\/12E"
            },
            {
            "firstName":"FIREARM, INTOXICATED LICENSEE CARRY c269 \u00a710H",
            "lastName":"269\/10H"
            },
            {
            "firstName":"FIREARM, INTOXICATED LICENSEE CARRY c269 \u00a710H",
            "lastName":"269\/10\/H1"
            },
            {
            "firstName":"FIREARM, LARCENY OF c. 266 s. 30",
            "lastName":"266.3"
            },
            {
            "firstName":"FIREARM, LARCENY OF c266 \u00a730(1)",
            "lastName":"266\/30\/E"
            },
            {
            "firstName":"FIREARM, POSSESS  c269 \u00a710(a)",
            "lastName":"269\/10\/A1"
            },
            {
            "firstName":"FIREARM, POSSESS LARGE CAPACITY c269 \u00a710(m)",
            "lastName":"269\/10\/AA"
            },
            {
            "firstName":"FIREARM, POSSESS LARGE CAPACITY FEEDING DEVICE c269 \u00a710(m)",
            "lastName":"269\/10\/AA1"
            },
            {
            "firstName":"FIREARM, POSSESS, SUBSEQUENT OFFENSE c269 \u00a710(d)",
            "lastName":"269\/10\/A11"
            },
            {
            "firstName":"FIREARM, SELL\/TRANSFER LARGE CAPACITY c269 \u00a710F(a)",
            "lastName":"269\/10F\/A"
            },
            {
            "firstName":"FIREARM, STORE IMPROP c140 \u00a7131L(a)&(b)",
            "lastName":"140\/131L\/A"
            },
            {
            "firstName":"FIREARM, STORE IMPROP LARGE CAPACITY c140 \u00a7131L(a)&(b)",
            "lastName":"140\/131L\/B"
            },
            {
            "firstName":"FIREARM, STORE IMPROP LARGE-CAPACITY NEAR MINOR c140 \u00a7131L(a)&(d)",
            "lastName":"140\/131L\/C"
            },
            {
            "firstName":"FIREARM, STORE IMPROPER c. 140 s. 131L(a) ",
            "lastName":"140.131L(a) "
            },
            {
            "firstName":"FIREARM, STORE IMPROPER LARGE CAPACITY c. 140 s. 131L(a)",
            "lastName":"140.131L(a) "
            },
            {
            "firstName":"FIREARM, STORE IMPROPER LARGE CAPACITY NEAR MINOR c. 140 s. 131L(a)",
            "lastName":"140.131L(a) "
            },
            {
            "firstName":"FIREARM\/LICENSE\/FID CARD, FAIL SURRENDER c. 269 s. 10(i)",
            "lastName":"269.10(i)"
            },
            {
            "firstName":"FIREARM\/LICENSE\/FID CARD, FAIL SURRENDER c269 \u00a710(i)",
            "lastName":"269\/10\/I"
            },
            {
            "firstName":"FIREARMS TO MINOR, SELL\/TRANSFER LARGE CAPACITY, c. 269 s. 10F(b)",
            "lastName":"269.10F(b)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 1 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(a)",
            "lastName":"269.10(a)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 1 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(c)",
            "lastName":"269.10(c)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 1 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(h)",
            "lastName":"269.10(h)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 2 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(a)",
            "lastName":"269.10(a)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 2 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(c)",
            "lastName":"269.10(c)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 3 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(a)",
            "lastName":"269.10(a)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 3 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(c)",
            "lastName":"269.10(c)"
            },
            {
            "firstName":"FIREARMS VIOL WITH 3 PRIOR VIOLENT\/DRUG CRIME c. 269 s. 10(h)",
            "lastName":"269.10(h)"
            },
            {
            "firstName":"FIREARMS WHILE OUI, LICENSEE CARRYING c. 269 s. 10H",
            "lastName":"269.10H"
            },
            {
            "firstName":"FIREARMS, DISTRIBUTION OF c269 \u00a710E(1)",
            "lastName":"269\/10E\/D"
            },
            {
            "firstName":"FIREARMS, SELL\/TRANSFER LARGE CAPACITY, c. 269 s. 10F(a)",
            "lastName":"269.10F(a)"
            },
            {
            "firstName":"FIREARMS, TRAFFICKING IN +19 c269 \u00a710E",
            "lastName":"269\/10E\/C"
            },
            {
            "firstName":"FIREARMS, TRAFFICKING IN 3-9 c269 \u00a710E",
            "lastName":"269\/10E\/A"
            },
            {
            "firstName":"FIREFIGHTER, INJURE c265 \u00a713D\u00bd",
            "lastName":"265\/13D12"
            },
            {
            "firstName":"FIREFIGHTER, INJURED c. 265 s. 13D\u00bd",
            "lastName":"265.13D\u00bd"
            },
            {
            "firstName":"FIREFIGHTER, INTERFERE WITH c. 268 s. 32A",
            "lastName":"268.32A"
            },
            {
            "firstName":"FIREFIGHTER, INTERFERE WITH c268 \u00a732A",
            "lastName":"268\/32A"
            },
            {
            "firstName":"FIREWORKS, EXPLODE WITHOUT BOND c148 \u00a742",
            "lastName":"148\/42"
            },
            {
            "firstName":"FIREWORKS, IMPROPER MANUFACTURE\/STORAGE c. 148 s. 40 through 44",
            "lastName":"148.40 through 44"
            },
            {
            "firstName":"FIREWORKS, POSSESS UNLAWFUL c148 \u00a739",
            "lastName":"148\/39\/A"
            },
            {
            "firstName":"FIREWORKS, SELL UNLAWFUL c. 148 s. 39",
            "lastName":"148.39"
            },
            {
            "firstName":"FIREWORKS, SELL UNLAWFUL c148 \u00a739",
            "lastName":"148\/39\/B"
            },
            {
            "firstName":"FISH, THROW OVERBOARD UPON INSPECTION c130 \u00a713",
            "lastName":"130\/13"
            },
            {
            "firstName":"FISH\/WILD ANIMAL, DEAL WITHOUT LIC c131 \u00a723",
            "lastName":"131\/23\/B"
            },
            {
            "firstName":"FISH\/WILDLIFE\u00bfFISHING VIOLATION 321 CMR \u00a74.07",
            "lastName":"321CMR407\/B"
            },
            {
            "firstName":"FISHERY, DISTURB c130 \u00a795",
            "lastName":"130\/95\/B"
            },
            {
            "firstName":"FISHING, COMMERCIAL LICENSE VIOL c. 130 s. 80",
            "lastName":"130.8"
            },
            {
            "firstName":"FISHING, COMMERCIAL LICENSE VIOL c130 \u00a780",
            "lastName":"130\/80\/B"
            },
            {
            "firstName":"FLARES VIOLATION BY COMMERCIAL VEHICLE * c85 \u00a714B",
            "lastName":"85\/14B"
            },
            {
            "firstName":"FLASHING SIGN IN VIOLATION OF DOH ORDER c. 85 s. 9A",
            "lastName":"85.9A"
            },
            {
            "firstName":"FLOTATION DEVICE VIOLATION 323 CMR \u00a72.07",
            "lastName":"323CMR207\/B"
            },
            {
            "firstName":"FOREIGN CORPORATION REPORT, FALSE c. 181 s. 13",
            "lastName":"181.13"
            },
            {
            "firstName":"FORGERY (Common Law)",
            "lastName":"COMLAW8"
            },
            {
            "firstName":"FORGERY OF BANK NOTE c267 \u00a78",
            "lastName":"267\/8\/A"
            },
            {
            "firstName":"FORGERY OF BANK NOTE OR TRAVELLER'S CHECK c. 267 s. 8",
            "lastName":"267.8"
            },
            {
            "firstName":"FORGERY OF CHECK c267 \u00a71",
            "lastName":"267\/1\/B"
            },
            {
            "firstName":"FORGERY OF COMMONWEALTH NOTE c267 \u00a77",
            "lastName":"267\/7"
            },
            {
            "firstName":"FORGERY OF DOCUMENT c267 \u00a71",
            "lastName":"267\/1\/A"
            },
            {
            "firstName":"FORGERY OF ORDER FOR MONEY c267 \u00a71",
            "lastName":"267\/1\/D"
            },
            {
            "firstName":"FORGERY OF PROMISSORY NOTE ENDORSEMENT c267 \u00a71",
            "lastName":"267\/1\/C"
            },
            {
            "firstName":"FORGERY OF TRAVELLER\u00bfS CHECK c267 \u00a78",
            "lastName":"267\/8\/B"
            },
            {
            "firstName":"FORGERY, CHECK FORGERY, PROMISSORY NOTE FORGERY c. 267 s. 1",
            "lastName":"267.1"
            },
            {
            "firstName":"FORTUNE TELLING, UNLICENSED c140 \u00a7185I",
            "lastName":"140\/185I"
            },
            {
            "firstName":"FRAUD\/CHEAT, GROSS c. 266 s. 76",
            "lastName":"266.76"
            },
            {
            "firstName":"FRAUD\/CHEAT, GROSS c266 \u00a776",
            "lastName":"266\/76"
            },
            {
            "firstName":"FUGITIVE FROM JUSTICE ON COURT WARRANT c276 \u00a720A",
            "lastName":"276\/20A"
            },
            {
            "firstName":"FUGITIVE FROM JUSTICE ON GOV'S WARRANT c276 \u00a719",
            "lastName":"276\/19\/A"
            },
            {
            "firstName":"FUGITIVE FROM JUSTICE WITHOUT WARRANT c276 \u00a720B",
            "lastName":"276\/20B"
            },
            {
            "firstName":"FUGITIVE, FAIL BRING BEFORE COURT c. 276 s. 19",
            "lastName":"276.19"
            },
            {
            "firstName":"FUGITIVE, FAIL BRING BEFORE COURT c276 \u00a719",
            "lastName":"276\/19\/B"
            },
            {
            "firstName":"FUNERAL DIRECTOR LEND USE OF NAME c114 \u00a745A",
            "lastName":"114\/45A"
            },
            {
            "firstName":"FUNERAL DIRECTOR, UNLICENSED c112 \u00a787",
            "lastName":"112\/87"
            },
            {
            "firstName":"FUNERAL PROCESSION, DISTURB c. 272 s. 42",
            "lastName":"272.42"
            },
            {
            "firstName":"FUNERAL PROCESSION, DISTURB c272 \u00a742",
            "lastName":"272\/42\/A"
            },
            {
            "firstName":"FUNERAL SERVICE, DISTURB c. 272 s. 42A",
            "lastName":"272.42A"
            },
            {
            "firstName":"FUNERAL SERVICE, DISTURB c272 \u00a742A",
            "lastName":"272\/42A"
            },
            {
            "firstName":"GAMBLING NUISANCE, MAINTAIN c139 \u00a714-\u00a715",
            "lastName":"139\/14"
            },
            {
            "firstName":"GAMING APPARATUS, KEEP c271 \u00a75",
            "lastName":"271\/5\/E"
            },
            {
            "firstName":"GAMING ENTERPRISE, MANAGE c271 \u00a716A",
            "lastName":"271\/16A"
            },
            {
            "firstName":"GAMING HOUSE, KEEP COMMON c271 \u00a75",
            "lastName":"271\/5\/A"
            },
            {
            "firstName":"GAMING HOUSE\/APPARATUS, KEEP OR PLAY\/PRESENT AT c. 271 s. 5",
            "lastName":"271.5"
            },
            {
            "firstName":"GAMING IN PUBLIC\/TRESPASSING c. 271 s. 2",
            "lastName":"271.2"
            },
            {
            "firstName":"GAMING IN PUBLIC\/TRESPASSING c271 \u00a72",
            "lastName":"271\/2\/A"
            },
            {
            "firstName":"GAMING IN PUBLIC\/TRESPASSING, ALLOW c271 \u00a72",
            "lastName":"271\/2\/B"
            },
            {
            "firstName":"GAMING, ALLOW PREMISES FOR c. 271 s. 3",
            "lastName":"271.3"
            },
            {
            "firstName":"GAMING, ALLOW PREMISES FOR c. 271 s. 8",
            "lastName":"271.8"
            },
            {
            "firstName":"GAMING, ALLOW PREMISES FOR c271 \u00a73",
            "lastName":"271\/3\/A"
            },
            {
            "firstName":"GAMING, ALLOW PREMISES FOR c271 \u00a78",
            "lastName":"271\/8\/A"
            },
            {
            "firstName":"GAMING, ALLOW PREMISES FOR, SUBSQ. OFF. c. 271 s. 3",
            "lastName":"271.3"
            },
            {
            "firstName":"GAMING, PLAY\/PRESENT AT c271 \u00a75",
            "lastName":"271\/5\/C"
            },
            {
            "firstName":"GARDEN\/ORCHARD\/NURSERY\/BOG, LARCENY FROM c266 \u00a7115",
            "lastName":"266\/115"
            },
            {
            "firstName":"GAS, FRAUDULENT USE OF c164 \u00a7126",
            "lastName":"164\/126\/B"
            },
            {
            "firstName":"GLASS IN BUILDING, BREAK c266 \u00a7114",
            "lastName":"266\/114\/A"
            },
            {
            "firstName":"GLASS, THROW ON BEACH c265 \u00a732",
            "lastName":"265\/32\/B"
            },
            {
            "firstName":"GLASS, THROW ON BEACH OR PUBLIC WAY c. 265 s. 32",
            "lastName":"265.32"
            },
            {
            "firstName":"GLASS, THROW ON PUBLIC WAY c265 \u00a732",
            "lastName":"265\/32\/A"
            },
            {
            "firstName":"GLUE TOXIC SUBSTANCE, INHALE c. 270 s. 18",
            "lastName":"270.18"
            },
            {
            "firstName":"GLUE\/TOXIC SUBSTANCE, INHALE c270 \u00a718",
            "lastName":"270\/18"
            },
            {
            "firstName":"GOLD, FRAUD IN FINENESS OF c266 \u00a778",
            "lastName":"266\/78\/A"
            },
            {
            "firstName":"GOLD\/SILVER\/PLATINUM RECORDS, FAIL KEEP c266 \u00a7142A",
            "lastName":"266\/142A"
            },
            {
            "firstName":"GRAVE PLANTING, VANDALIZE c272 \u00a773",
            "lastName":"272\/73\/B"
            },
            {
            "firstName":"GRAVE, DISTURB c272 \u00a773",
            "lastName":"272\/73\/A"
            },
            {
            "firstName":"GRAVE, GRAVESTONE OR PLANTING, DAMAGE c. 272 s. 73",
            "lastName":"272.73"
            },
            {
            "firstName":"GRAVESTONE, VANDALIZE c272 \u00a773",
            "lastName":"272\/73\/C"
            },
            {
            "firstName":"HABITUAL OFFENDER c279 \u00a725",
            "lastName":"279C\/25"
            },
            {
            "firstName":"HANDICAP PARKING PLATE MISUSE * c90 \u00a72",
            "lastName":"90\/2\/B"
            },
            {
            "firstName":"HANG ONTO MV c90 \u00a713",
            "lastName":"90\/13\/B"
            },
            {
            "firstName":"HANG ONTO MV, 2ND OFFENSE c90 \u00a713",
            "lastName":"90\/13\/C"
            },
            {
            "firstName":"HARASSMENT PREVENTION ORDER, VIOLATE c258 \u00a79",
            "lastName":"258\/9"
            },
            {
            "firstName":"HARASSMENT, CRIMINAL c265 \u00a743A(a)",
            "lastName":"265\/43A\/A"
            },
            {
            "firstName":"HARASSMENT, CRIMINAL, SUBSQ.OFF.  c265 \u00a743A(b)",
            "lastName":"265\/43A\/B"
            },
            {
            "firstName":"HARMFUL SUBSTANCE, DISTRIBUTE FOOD WITH c270 \u00a78A",
            "lastName":"270\/8A"
            },
            {
            "firstName":"HARMFUL SUBSTANCE, PEDDLE c270 \u00a73",
            "lastName":"270\/3"
            },
            {
            "firstName":"HARSH & OBJECTIONABLE",
            "lastName":"90\/16\/A"
            },
            {
            "firstName":"HAWKERS & PEDDLERS FAILURE TO REGISTER",
            "lastName":"51211|16-5.1"
            },
            {
            "firstName":"HAZARDOUS MATERIALS TRANSPORT VIOL * 540 CMR \u00a714.03",
            "lastName":"540CMR1403\/A"
            },
            {
            "firstName":"HAZARDOUS WASTE RELEASE, FL NOTIFY DEP c21E \u00a77",
            "lastName":"21E\/7"
            },
            {
            "firstName":"HAZARDOUS WASTE VIOLATION c. 21E s. 11",
            "lastName":"21E.11"
            },
            {
            "firstName":"HAZARDOUS WASTE VIOLATION c21C \u00a75",
            "lastName":"21C\/5"
            },
            {
            "firstName":"HAZARDOUS WASTE VIOLATION c21E \u00a711",
            "lastName":"21E\/11"
            },
            {
            "firstName":"HAZING c269 \u00a717",
            "lastName":"269\/17"
            },
            {
            "firstName":"HAZING, FAIL REPORT c269 \u00a718",
            "lastName":"269\/18"
            },
            {
            "firstName":"HEADLIGHTS, ALTERNATING FLASHING * 540 CMR \u00a722.05(2)",
            "lastName":"540CMR2205\/B"
            },
            {
            "firstName":"HEADLIGHTS, FAIL DIM * 540 CMR \u00a72.12(2)",
            "lastName":"540CMR212"
            },
            {
            "firstName":"HEADLIGHTS, FAIL DIM * 540 CMR \u00a722.05(2)",
            "lastName":"540CMR2205"
            },
            {
            "firstName":"HEALTH CARE CLAIM, FALSE c175H \u00a72",
            "lastName":"175H\/2"
            },
            {
            "firstName":"HEALTH\/WELFARE FUND, UNAPPROVED c151D \u00a72",
            "lastName":"151D\/2\/B"
            },
            {
            "firstName":"HEIGHT, MODIFY MV c90 \u00a77P",
            "lastName":"90\/7P\/B"
            },
            {
            "firstName":"HEIGHT, MODIFY MV, 2ND OFFENSE c90 \u00a77P",
            "lastName":"90\/7P\/C"
            },
            {
            "firstName":"HEIGHT, OPERATE MV WITH MODIFIED * c90 \u00a77P",
            "lastName":"90\/7P\/A"
            },
            {
            "firstName":"HEROIN, BEING PRESENT WHERE KEPT c. 94C s. 35",
            "lastName":"94C.35"
            },
            {
            "firstName":"HEROIN, BEING PRESENT WHERE KEPT c94C \u00a735",
            "lastName":"94C\/35"
            },
            {
            "firstName":"HEROIN, POSSESS c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"HEROIN, POSSESS c94C \u00a734",
            "lastName":"94C\/34\/J"
            },
            {
            "firstName":"HEROIN, POSSESS, SUBSQ. OFF. c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"HEROIN, POSSESS, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/K"
            },
            {
            "firstName":"HEROIN, TRAFFICKING IN, OVER 100 GRAMS c94C \u00a732E(c)(3)",
            "lastName":"94C\/32E\/B3"
            },
            {
            "firstName":"HEROIN, TRAFFICKING IN, OVER 14 GRAMS c94C \u00a732E(c)(1)",
            "lastName":"94C\/32E\/B1"
            },
            {
            "firstName":"HEROIN, TRAFFICKING IN, OVER 200 GRAMS c94C \u00a732E(c)(4)",
            "lastName":"94C\/32E\/B4"
            },
            {
            "firstName":"HEROIN, TRAFFICKING IN, OVER 28 GRAMS c94C \u00a732E(c)(2)",
            "lastName":"94C\/32E\/B2"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICK IN c. 94C s. 32E(c)(1) - 14 to 28 g",
            "lastName":"94C.32E(c)(1)"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICK IN c. 94C s. 32E(c)(2) - 28 to 100 g",
            "lastName":"94C.32E(c)(2)"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICK IN c. 94C s. 32E(c)(3) - 100 to 200 g",
            "lastName":"94C.32E(c)(3)"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICK IN c. 94C s. 32E(c)(4) - 200 or more g",
            "lastName":"94C.32E(c)(4)"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICKING IN c94C \u00a732E(c)",
            "lastName":"94C\/32E\/B"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICKING IN, 100 GRAMS OR MORE c94C \u00a732E(c)",
            "lastName":"94C\/32E\/G"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICKING IN, 18 GRAMS OR MORE C94c \u00a732E(c)",
            "lastName":"94C\/32E\/E0"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICKING IN, 18 GRAMS OR MORE LESS 36 C94c \u00a732E(c)",
            "lastName":"94C\/32E\/EE"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICKING IN, 200 GRAMS OR MORE C94c \u00a732E(c)",
            "lastName":"94C\/32E\/H"
            },
            {
            "firstName":"HEROIN\/MORPHINE\/OPIUM, TRAFFICKING IN, 36 GRAMS OR MORE LESS 100 C94c \u00a732E(c)",
            "lastName":"94C\/32E\/F"
            },
            {
            "firstName":"HIRING VEHICLE, FRAUD IN c. 266 s. 64",
            "lastName":"266.64"
            },
            {
            "firstName":"HIRING VEHICLE, FRAUD IN c266 \u00a764",
            "lastName":"266\/64"
            },
            {
            "firstName":"HISTORIC MARKER\/MONUMENT, VANDALIZE c266 \u00a795",
            "lastName":"266\/95"
            },
            {
            "firstName":"HOME IMPROVEMENT CONTRACTOR VIOLATION c. 142A s. 19",
            "lastName":"142A.19"
            },
            {
            "firstName":"HOME IMPROVEMENT CONTRACTOR VIOLATION c142A \u00a719",
            "lastName":"142A\/19\/A"
            },
            {
            "firstName":"HOME IMPROVEMENT CONTRACTOR, UNLICENSED c. 142A s. 19",
            "lastName":"142A.19"
            },
            {
            "firstName":"HOME IMPROVEMENT CONTRACTOR, UNLICENSED c142A \u00a719",
            "lastName":"142A\/19\/B"
            },
            {
            "firstName":"HOME INVASION",
            "lastName":"21113|265-18(C)"
            },
            {
            "firstName":"HOME INVASION",
            "lastName":"266\/14"
            },
            {
            "firstName":"HOME INVASION c. 265 s. 18C (The interpretation of \"statutory minimum\" may be affected by Com. v. Brown, 47 Mass. App. Ct. 616 (1999))",
            "lastName":"265.18C"
            },
            {
            "firstName":"HOME INVASION c265 \u00a718C",
            "lastName":"265\/18C\/A"
            },
            {
            "firstName":"HOME INVASION, ARMED, FIREARM c. 265 s. 18C",
            "lastName":"265.18C"
            },
            {
            "firstName":"HOME INVASION, ARMED, FIREARM SUBSQ. OFF. c. 265 s. 18C",
            "lastName":"265.18C"
            },
            {
            "firstName":"HOME INVASION, FIREARM-ARMED c265 \u00a718C",
            "lastName":"265\/18C\/C"
            },
            {
            "firstName":"HOME INVASION, SUBSQ. OFF. c. 265 s. 18C",
            "lastName":"265.18C"
            },
            {
            "firstName":"HOME INVASION, SUBSQ.OFF.  c265 \u00a718C",
            "lastName":"265\/18C\/B"
            },
            {
            "firstName":"HORN VIOLATION, MV * c90 \u00a77",
            "lastName":"90\/7\/B"
            },
            {
            "firstName":"HOTEL REGISTER, FAIL KEEP c140 \u00a727",
            "lastName":"140\/27"
            },
            {
            "firstName":"HUNT ON PUBL LAND WITHOUT PERMIT c131 \u00a759",
            "lastName":"131\/59\/B"
            },
            {
            "firstName":"HUNT\/FISH IN CLOSED SEASON c131 \u00a75",
            "lastName":"131\/5\/B"
            },
            {
            "firstName":"HUNT\/FISH WITHOUT LICENSE c131 \u00a711",
            "lastName":"131\/11\/B"
            },
            {
            "firstName":"HYDROMORPHONE, TRAFFICKING IN, OVER 100 GRAMS c94C \u00a732E(c)",
            "lastName":"94C\/32E\/C3"
            },
            {
            "firstName":"HYDROMORPHONE, TRAFFICKING IN, OVER 18 GRAMS c94C \u00a732E(c)",
            "lastName":"94C\/32E\/C1"
            },
            {
            "firstName":"HYDROMORPHONE, TRAFFICKING IN, OVER 200 GRAMS c94C \u00a732E(c)",
            "lastName":"94C\/32E\/C4"
            },
            {
            "firstName":"HYDROMORPHONE, TRAFFICKING IN, OVER 36 GRAMS c94C \u00a732E(c)",
            "lastName":"94C\/32E\/C2"
            },
            {
            "firstName":"HYPODERMIC SALES RECORD, FL KEEP c94C \u00a727(d)",
            "lastName":"94C\/27\/A"
            },
            {
            "firstName":"HYPODERMIC, OBTAIN WITHOUT LIC, SUBSQ. c94C \u00a727(e)",
            "lastName":"94C\/27\/H"
            },
            {
            "firstName":"HYPODERMIC, POSSESS c94C \u00a727(a)",
            "lastName":"94C\/27\/I"
            },
            {
            "firstName":"HYPODERMIC, POSSESS, SUBSQ.OFF. c94C \u00a727(a)",
            "lastName":"94C\/27\/J"
            },
            {
            "firstName":"HYPODERMIC, STORE IMPROP c94C \u00a727(b)",
            "lastName":"94C\/27\/K"
            },
            {
            "firstName":"HYPODERMIC, VIOLATION c. 94C s. 27",
            "lastName":"94C.27"
            },
            {
            "firstName":"HYPODERMIC, VIOLATION, SUBSQ. OFF. c. 94C s. 27",
            "lastName":"94C.27"
            },
            {
            "firstName":"IDENTIFY SELF, MV OPERATOR REFUSE c90 \u00a725",
            "lastName":"90\/25\/A"
            },
            {
            "firstName":"IDENTIFY SELF, REFUSE c40 \u00a721D(c)",
            "lastName":"40\/21D\/A"
            },
            {
            "firstName":"IDENTITY FRAUD c266 \u00a737E",
            "lastName":"266\/37E"
            },
            {
            "firstName":"IDENTITY FRAUD, POSSESS TOOLS W\/INTENT c266 \u00a737Ec1\/2",
            "lastName":"266\/37E\/B"
            },
            {
            "firstName":"IDLE ENGINE OF STOPPED MV OVER 5 MINUTES * c90 \u00a716A",
            "lastName":"90\/16A"
            },
            {
            "firstName":"IGNITION INTERLOCK, OPERATE WITHOUT c90 \u00a724S",
            "lastName":"90\/24\/S2"
            },
            {
            "firstName":"ILLGL POSS CLASS A SUBSTANCE",
            "lastName":"94C\/33"
            },
            {
            "firstName":"ILLGL POSS CLASS C SUBSTANCE",
            "lastName":"94C\/34"
            },
            {
            "firstName":"IMPROPER OPERATION OF MV, ALLOW * c90 \u00a712",
            "lastName":"90\/12"
            },
            {
            "firstName":"INCEST c. 272 s. 17",
            "lastName":"272.17"
            },
            {
            "firstName":"INCEST c272 \u00a717",
            "lastName":"272\/17"
            },
            {
            "firstName":"INDECENT A&B ON CHILD UNDER 14 AFTER CERTAIN OFFENSES c265 \u00a713B",
            "lastName":"265\/13B\/C"
            },
            {
            "firstName":"INDECENT A&B ON CHILD UNDER 14 c. 265 s. 13B ",
            "lastName":"265.13B"
            },
            {
            "firstName":"INDECENT A&B ON CHILD UNDER 14 c265 \u00a713B",
            "lastName":"265\/13B\/A"
            },
            {
            "firstName":"INDECENT A&B ON CHILD UNDER 14, SUBSQ. c265 \u00a713B",
            "lastName":"265\/13B\/B"
            },
            {
            "firstName":"INDECENT A&B ON CHILD UNDER 14, SUBSQ. OFF. c. 265 s. 13B",
            "lastName":"265.13B"
            },
            {
            "firstName":"INDECENT A&B ON DISABLED PERSON OVER 60 c265 \u00a713H\/C",
            "lastName":"265\/13H\/C"
            },
            {
            "firstName":"INDECENT A&B ON PERSON 14 OR OVER AFTER CERTAIN OFFENSES  c265 \u00a713H",
            "lastName":"265\/13H\/B"
            },
            {
            "firstName":"INDECENT A&B ON PERSON 14 OR OVER c. 265 s. 13H",
            "lastName":"265.13H"
            },
            {
            "firstName":"INDECENT A&B ON PERSON 14 OR OVER c265 \u00a713H",
            "lastName":"265\/13H"
            },
            {
            "firstName":"INDECENT A&B ON RETARDED PERSON c. 265 s. 13F",
            "lastName":"265.13F"
            },
            {
            "firstName":"INDECENT A&B ON RETARDED PERSON c265 \u00a713F",
            "lastName":"265\/13F\/A"
            },
            {
            "firstName":"INDECENT EXPOSURE c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"INDECENT EXPOSURE c272 \u00a753",
            "lastName":"272\/53\/H"
            },
            {
            "firstName":"INFERNAL MACHINE, POSSESS c. 266 s. 102A",
            "lastName":"266.102A"
            },
            {
            "firstName":"INFERNAL MACHINE, POSSESS c266 \u00a7102A",
            "lastName":"266\/102A"
            },
            {
            "firstName":"INNKEEPER, DEFRAUD, OVER $100 c. 140 s. 12",
            "lastName":"140.12"
            },
            {
            "firstName":"INNKEEPER, DEFRAUD, OVER $100 c140 \u00a712",
            "lastName":"140\/12\/B"
            },
            {
            "firstName":"INNKEEPER, DEFRAUD, UNDER $100 c. 140 s. 12",
            "lastName":"140.12"
            },
            {
            "firstName":"INNKEEPER, DEFRAUD, UNDER $100 c140 \u00a712",
            "lastName":"140\/12\/C"
            },
            {
            "firstName":"INNKEEPER\/RESTAURANT, UNLICENSED, 3RD AND SUBSQ. OFF. c. 140 s. 20",
            "lastName":"140.2"
            },
            {
            "firstName":"INSPECTION CERTIFICATE, FALSE EMISSIONS c111 \u00a7142M",
            "lastName":"111\/142M\/B"
            },
            {
            "firstName":"INSPECTION CERTIFICATE, IMPROPER MV c111 \u00a7142M",
            "lastName":"111\/142M\/C"
            },
            {
            "firstName":"INSPECTION\/STICKER, NO * c90 \u00a720",
            "lastName":"90\/20\/B"
            },
            {
            "firstName":"INSPECTOR, OBSTRUCT DIV OF STANDARDS c. 6A s. 13",
            "lastName":"6A.13"
            },
            {
            "firstName":"INSURANCE CERTIFICATE, FALSE MOTOR VEH c. 90 s. 34B",
            "lastName":"90.34B"
            },
            {
            "firstName":"INSURANCE CERTIFICATE, FALSE MV c90 \u00a734B",
            "lastName":"90\/34B\/A"
            },
            {
            "firstName":"INSURANCE CERTIFICATE, ISSUE IMPROPER MV c90 \u00a734B",
            "lastName":"90\/34B\/B"
            },
            {
            "firstName":"INSURANCE CLAIM, FALSE LIFE c175 \u00a7127",
            "lastName":"175\/127\/A"
            },
            {
            "firstName":"INSURANCE CLAIM, FALSE MOTOR VEH c. 266 s. 111B",
            "lastName":"266.111B"
            },
            {
            "firstName":"INSURANCE CLAIM, FALSE MOTOR VEH c266 \u00a7111B",
            "lastName":"266\/111B"
            },
            {
            "firstName":"INSURANCE CLAIM, PREPARE FALSE c266 \u00a7111A",
            "lastName":"266\/111A\/B"
            },
            {
            "firstName":"INSURANCE CLAIM, PREPARE OR PRESENT FALSE c. 266 s. 111A",
            "lastName":"266.111A"
            },
            {
            "firstName":"INSURANCE CLAIM, PRESENT FALSE c266 \u00a7111A",
            "lastName":"266\/111A\/A"
            },
            {
            "firstName":"INSURANCE INFO, GET ON FALSE PRETENSES c175I \u00a722",
            "lastName":"175I\/22"
            },
            {
            "firstName":"INSURANCE VIOLATION c175 \u00a7194",
            "lastName":"175\/194"
            },
            {
            "firstName":"INTIMIDATE TO STEAL FROM DEPOSITORY c265 \u00a721",
            "lastName":"265\/21\/A"
            },
            {
            "firstName":"INTIMIDATE TO STEAL FROM DEPOSITORY, ATT c265 \u00a721",
            "lastName":"265\/21\/B"
            },
            {
            "firstName":"INTIMIDATION OF A WITNESS",
            "lastName":"268\/13B"
            },
            {
            "firstName":"IRRIGATION EQUIPMENT, DAMAGE c. 266 s. 138A",
            "lastName":"266.138A"
            },
            {
            "firstName":"JET SKI AT NIGHT c90B \u00a79A",
            "lastName":"90B\/9A\/B"
            },
            {
            "firstName":"JUNIOR OPERATOR OP 12-5 AM W\/O PARENT c90 \u00a7\u00a78 & 10",
            "lastName":"90\/10\/D"
            },
            {
            "firstName":"JUNIOR OPERATOR WITH PASSENGER UNDER 18 * c90 \u00a78",
            "lastName":"90\/8\/E"
            },
            {
            "firstName":"JUNK DEALER, UNLICENSED c140 \u00a755",
            "lastName":"140\/55"
            },
            {
            "firstName":"JUROR FAIL TO ATTEND c234 \u00a736",
            "lastName":"234\/36"
            },
            {
            "firstName":"JUROR FAIL TO ATTEND c234A \u00a742",
            "lastName":"234A\/42"
            },
            {
            "firstName":"JUROR PROCESSING, FRAUD IN c. 234A s. 71",
            "lastName":"234A.71"
            },
            {
            "firstName":"JUROR QUESTIONNAIRE, FALSE STATEMENT IN c234A \u00a732",
            "lastName":"234A\/32"
            },
            {
            "firstName":"JUROR, ATTEMPT TO BRIBE c268 \u00a713",
            "lastName":"268\/13\/B"
            },
            {
            "firstName":"JUROR, BRIBE c268 \u00a713",
            "lastName":"268\/13\/A"
            },
            {
            "firstName":"JUROR, INTIMIDATE c268 \u00a713B",
            "lastName":"268\/13B\/C"
            },
            {
            "firstName":"JUROR\/MASTER\/ARBITRATOR\/REFEREE, BRIBE OR ATTEMPT TO BRIBE c. 268 s. 13",
            "lastName":"268.13"
            },
            {
            "firstName":"JUROR\/WITNESS, INTIMIDATE OR RETALIATE c. 268 s. 13B",
            "lastName":"268.13B"
            },
            {
            "firstName":"JURY LIST, SOLICIT ADDING NAME TO c. 234 s. 38",
            "lastName":"234.38"
            },
            {
            "firstName":"KDNPPNG",
            "lastName":"265\/26"
            },
            {
            "firstName":"KEEP RIGHT FOR ONCOMING MV, FAIL TO * c89 \u00a71",
            "lastName":"89\/1"
            },
            {
            "firstName":"KEEP RIGHT ON HILL\/OBSTRUCTED VIEW, FL * c89 \u00a74",
            "lastName":"89\/4"
            },
            {
            "firstName":"KEEPING GAMING APPARATUS c271 \u00a717",
            "lastName":"271\/17"
            },
            {
            "firstName":"KIDNAPPING & ENDANGER INCOMPETENT OR CHILD BY RELATIVE c. 265 s. 26A",
            "lastName":"265.26A"
            },
            {
            "firstName":"KIDNAPPING & ENDANGER MINOR BY RELATIVE c265 \u00a726A",
            "lastName":"265\/26A\/B"
            },
            {
            "firstName":"KIDNAPPING & ENDANGER PERSON IN CUSTODY c265 \u00a726A",
            "lastName":"265\/26A\/D"
            },
            {
            "firstName":"KIDNAPPING c. 265 s. 26",
            "lastName":"265.26"
            },
            {
            "firstName":"KIDNAPPING c265 \u00a726",
            "lastName":"265\/26\/A"
            },
            {
            "firstName":"KIDNAPPING FOR EXTORTION c265 \u00a709",
            "lastName":"265\/26\/B"
            },
            {
            "firstName":"KIDNAPPING FOR EXTORTION, FIREARM-ARMED c265 \u00a726",
            "lastName":"265\/26\/C"
            },
            {
            "firstName":"KIDNAPPING INCOMPETENT OR CHILD BY RELATIVE c. 265 s. 26A",
            "lastName":"265.26A"
            },
            {
            "firstName":"KIDNAPPING MINOR BY RELATIVE c265 \u00a726A",
            "lastName":"265\/26A\/A"
            },
            {
            "firstName":"KIDNAPPING OF CHILD c265 \u00a726",
            "lastName":"265\/26\/G"
            },
            {
            "firstName":"KIDNAPPING PERSON IN CUSTODY c265 \u00a726A",
            "lastName":"265\/26A\/C"
            },
            {
            "firstName":"KIDNAPPING WITH SERIOUS BODILY INJURY, ARMED c265 \u00a726",
            "lastName":"265\/26\/D"
            },
            {
            "firstName":"KIDNAPPING WITH SEXUAL ASSAULT, ARMED c. 265 s. 26",
            "lastName":"265.26"
            },
            {
            "firstName":"KIDNAPPING WITH SEXUAL ASSAULT, ARMED c265 \u00a726",
            "lastName":"265\/26\/E"
            },
            {
            "firstName":"KIDNAPPING, ARMED, FIREARM c. 265 s. 26",
            "lastName":"265.26"
            },
            {
            "firstName":"KIDNAPPING, FIREARM-ARMED c265 \u00a726",
            "lastName":"265\/26\/F"
            },
            {
            "firstName":"LANDLORD INTERFERE WITH QUIET ENJOYMENT c186 \u00a714",
            "lastName":"186\/14\/C"
            },
            {
            "firstName":"LANDLORD, WRONGFUL ACTS c. 186 s. 14",
            "lastName":"186.14"
            },
            {
            "firstName":"LARC. FR A PERSON 65 OR OVER",
            "lastName":"266\/25"
            },
            {
            "firstName":"LARC. OF A MV OR TRAILER",
            "lastName":"266\/28"
            },
            {
            "firstName":"LARC. PROP. OVER $250(VAR)",
            "lastName":"266\/30"
            },
            {
            "firstName":"LARCENY BY CHECK OVER $1200 c266 \u00a737 & \u00a730(1)",
            "lastName":"266\/37\/A1"
            },
            {
            "firstName":"LARCENY BY CHECK OVER $250 c. 266 s. 37 ",
            "lastName":"266.37"
            },
            {
            "firstName":"LARCENY BY CHECK OVER $250 c266 \u00a737 & \u00a730(1)",
            "lastName":"266\/37\/A"
            },
            {
            "firstName":"LARCENY BY CHECK UNDER $1200 c266 \u00a737 & \u00a730(1)",
            "lastName":"266\/37\/B1"
            },
            {
            "firstName":"LARCENY BY CHECK UNDER $250 c. 266 s. 37",
            "lastName":"266.37"
            },
            {
            "firstName":"LARCENY BY CHECK UNDER $250 c266 \u00a737 & \u00a730(1)",
            "lastName":"266\/37\/B"
            },
            {
            "firstName":"LARCENY BY SINGLE SCHEME, ATTEMPTED c266 \u00a730L",
            "lastName":"266\/30\/L"
            },
            {
            "firstName":"LARCENY FROM BUILDING c266 \u00a720",
            "lastName":"266\/20\/A"
            },
            {
            "firstName":"LARCENY FROM ELDER\/DISABLED PERSON; $250.00 OR UNDER c. 266 s. 30(5)",
            "lastName":"266.30(5)"
            },
            {
            "firstName":"LARCENY FROM ELDER\/DISABLED PERSON; OVER $250.00 c. 266 s. 30(5)",
            "lastName":"266.30(5)"
            },
            {
            "firstName":"LARCENY FROM PERSON +65 c. 266 s. 25",
            "lastName":"266.25"
            },
            {
            "firstName":"LARCENY FROM PERSON +65 c266 \u00a725(a)",
            "lastName":"266\/25\/B"
            },
            {
            "firstName":"LARCENY FROM PERSON +65, SUBSQ. OFF. c. 266 s. 25",
            "lastName":"266.25"
            },
            {
            "firstName":"LARCENY FROM PERSON +65, SUBSQ.OFF. c266 \u00a725(a)",
            "lastName":"266\/25\/C"
            },
            {
            "firstName":"LARCENY FROM PERSON c. 266 s. 25",
            "lastName":"266.25"
            },
            {
            "firstName":"LARCENY FROM PERSON c266 \u00a725(b)",
            "lastName":"266\/25\/A"
            },
            {
            "firstName":"LARCENY OF AUTO ACC. OVER $250",
            "lastName":"21412|266-30"
            },
            {
            "firstName":"LARCENY OVER $1200 BY SINGLE SCHEME c266 \u00a730(1)",
            "lastName":"266\/30\/B"
            },
            {
            "firstName":"LARCENY OVER $1200 c266 \u00a730(1)",
            "lastName":"266\/30\/A"
            },
            {
            "firstName":"LARCENY OVER $250 BY BOAT CAPTAIN  c266 \u00a732 & \u00a730(1)",
            "lastName":"266\/32\/A"
            },
            {
            "firstName":"LARCENY OVER $250 BY BOAT CAPTAIN c. 266 s. 32 ",
            "lastName":"266.32"
            },
            {
            "firstName":"LARCENY OVER $250 BY FALSE PRETENSE c. 266 s. 34 ",
            "lastName":"266.34"
            },
            {
            "firstName":"LARCENY OVER $250 BY FALSE PRETENSE c266 \u00a734 & \u00a730(1)",
            "lastName":"266\/34\/A"
            },
            {
            "firstName":"LARCENY OVER $250 BY SINGLE SCHEME c. 266 s. 30 ",
            "lastName":"266.3"
            },
            {
            "firstName":"LARCENY OVER $250 BY SINGLE SCHEME c266 \u00a730(1)",
            "lastName":"266\/30\/B"
            },
            {
            "firstName":"LARCENY OVER $250 c. 266 s. 30 ",
            "lastName":"266.3"
            },
            {
            "firstName":"LARCENY OVER $250 c266 \u00a730(1)",
            "lastName":"266\/30\/A"
            },
            {
            "firstName":"LARCENY OVER $250 FROM +60\/DISABLED c266 \u00a730(5)",
            "lastName":"266\/30\/I"
            },
            {
            "firstName":"LARCENY UNDER $1200 BY SINGLE SCHEME c266 \u00a730(1)",
            "lastName":"266\/30\/D"
            },
            {
            "firstName":"LARCENY UNDER $1200 c266 \u00a730(1)",
            "lastName":"266\/30\/C"
            },
            {
            "firstName":"LARCENY UNDER $250 BY BOAT CAPTAIN c. 266 s. 32",
            "lastName":"266.32"
            },
            {
            "firstName":"LARCENY UNDER $250 BY BOAT CAPTAIN c266 \u00a732 & \u00a730(1)",
            "lastName":"266\/32\/B"
            },
            {
            "firstName":"LARCENY UNDER $250 BY FALSE PRETENSE c. 266 s. 34",
            "lastName":"266.34"
            },
            {
            "firstName":"LARCENY UNDER $250 BY FALSE PRETENSE c266 \u00a734 & \u00a730(1)",
            "lastName":"266\/34\/B"
            },
            {
            "firstName":"LARCENY UNDER $250 BY SINGLE SCHEME c. 266 s. 30",
            "lastName":"266.3"
            },
            {
            "firstName":"LARCENY UNDER $250 BY SINGLE SCHEME c266 \u00a730 & \u00a730(1)",
            "lastName":"266\/30\/D"
            },
            {
            "firstName":"LARCENY UNDER $250 c. 266 s. 30",
            "lastName":"266.3"
            },
            {
            "firstName":"LARCENY UNDER $250 c266 \u00a730(1)",
            "lastName":"266\/30\/C"
            },
            {
            "firstName":"LARCENY UNDER $250 FROM +60\/DISABLED c266 \u00a730(5)",
            "lastName":"266\/30\/J"
            },
            {
            "firstName":"LARCENY, ATTEMPTED c266 \u00a730",
            "lastName":"266\/30\/K"
            },
            {
            "firstName":"LAW, REMOVED ATTORNEY PRACTICE c221 \u00a741",
            "lastName":"221\/41\/A"
            },
            {
            "firstName":"LAW, UNAUTHORIZED PRACTICE OF c. 221 s. 41",
            "lastName":"221.41"
            },
            {
            "firstName":"LAW, UNAUTHORIZED PRACTICE OF c221 \u00a741",
            "lastName":"221\/41\/C"
            },
            {
            "firstName":"LEAD PAINT ABATEMENT ORDER, FAIL OBEY c111 \u00a7197",
            "lastName":"111\/197\/A"
            },
            {
            "firstName":"LEAD PAINT, FAIL ABATE\/CONTAIN c111 \u00a7197",
            "lastName":"111\/197\/B"
            },
            {
            "firstName":"LEARNERS PERMIT VIOLATION * c90 \u00a78B",
            "lastName":"90\/8B"
            },
            {
            "firstName":"LEASE MV LESSEE ALLOW UNAUTH PERSON OP c90 \u00a732E",
            "lastName":"90\/32E\/B"
            },
            {
            "firstName":"LEASE MV LESSEE FAIL RETURN MV c90 \u00a732C",
            "lastName":"90\/32C\/C"
            },
            {
            "firstName":"LEASE MV LESSOR FAIL MAINTAIN INSURANCE c90 \u00a732E",
            "lastName":"90\/32E\/A"
            },
            {
            "firstName":"LEASE MV OBTAINED BY FRAUD\/BAD CHECK c90 \u00a732F",
            "lastName":"90\/32F"
            },
            {
            "firstName":"LEASE MV VIOLATIONS c. 90 s. 32C",
            "lastName":"90.32C"
            },
            {
            "firstName":"LEASE MV VIOLATIONS c. 90 s. 32E",
            "lastName":"90.32E"
            },
            {
            "firstName":"LEASED PERSONALTY, CONCEAL\/SELL\/PLEDGE c266 \u00a787",
            "lastName":"266\/87\/A"
            },
            {
            "firstName":"LEASED PERSONALTY, CONCEAL\/SELL\/PLEDGE\/FAIL RETURN c. 266 s. 87",
            "lastName":"266.87"
            },
            {
            "firstName":"LEASED PERSONALTY, FAIL RETURN c266 \u00a787",
            "lastName":"266\/87\/B"
            },
            {
            "firstName":"LEAVE SCENE OF PERSONAL INJURY & DEATH c. 90 s. 24(2)(a\u00bd)(2)",
            "lastName":"90.24(2)(a\u00bd)(2)"
            },
            {
            "firstName":"LEAVE SCENE OF PERSONAL INJURY & DEATH c90 \u00a724(2)(a\u00bd)(2)",
            "lastName":"90\/24\/B"
            },
            {
            "firstName":"LEAVE SCENE OF PERSONAL INJURY c. 90 s. 24(2)(a\u00bd)(1)",
            "lastName":"90.24(2)(a\u00bd)(1)"
            },
            {
            "firstName":"LEAVE SCENE OF PERSONAL INJURY c90 \u00a724(2)(a\u00bd)(1)",
            "lastName":"90\/24\/A"
            },
            {
            "firstName":"LEAVE SCENE OF PROPERTY DAMAGE c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"LEAVE SCENE OF PROPERTY DAMAGE c90 \u00a724(2)(a)",
            "lastName":"90\/24\/C"
            },
            {
            "firstName":"LEFT LANE RESTRICTION VIOLATION * c89 \u00a74C",
            "lastName":"89\/4C"
            },
            {
            "firstName":"LEGAL NOTICE, VANDALIZE c266 \u00a7124",
            "lastName":"266\/124"
            },
            {
            "firstName":"LEWD, WANTON & LASCIVIOUS CONDUCT c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"LEWD, WANTON & LASCIVIOUS CONDUCT c272 \u00a753",
            "lastName":"272\/53\/E"
            },
            {
            "firstName":"LEWDNESS, OPEN AND GROSS c. 272 s. 16",
            "lastName":"272.16"
            },
            {
            "firstName":"LEWDNESS, OPEN AND GROSS c272 \u00a716",
            "lastName":"272\/16"
            },
            {
            "firstName":"LEWDNESS, OPEN AND GROSS, SUBSQ.OFF.  c272 \u00a716",
            "lastName":"272\/16\/B"
            },
            {
            "firstName":"LIBRARY MATERIALS, FAIL RETURN c266 \u00a799A",
            "lastName":"266\/99A\/C"
            },
            {
            "firstName":"LIBRARY, DISTURB c272 \u00a741",
            "lastName":"272\/41"
            },
            {
            "firstName":"LIC. UNDER c. 131, ALTER\/FORGE c. 131 s. 33",
            "lastName":"131.33"
            },
            {
            "firstName":"LICENSE CLASS, OPERATE MV IN VIOLATION c90 \u00a710",
            "lastName":"90\/10\/B"
            },
            {
            "firstName":"LICENSE NOT IN POSSESSION * c90 \u00a711",
            "lastName":"90\/11\/A"
            },
            {
            "firstName":"LICENSE RESTRICTION, OPERATE MV IN VIOL c90 \u00a710",
            "lastName":"90\/10\/C"
            },
            {
            "firstName":"LICENSE RESTRICTION, OPERATING MOTOR VEHICLE IN VIOLATION c. 90 s. 10",
            "lastName":"90. 10"
            },
            {
            "firstName":"LICENSE REVOKED AS HTO, OPERATE MV WITH c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"LICENSE REVOKED AS HTO, OPERATE MV WITH c90 \u00a723",
            "lastName":"90\/23\/C"
            },
            {
            "firstName":"LICENSE SUSPENDED FOR OUI, OPER MV WITH c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"LICENSE SUSPENDED FOR OUI, OPER MV WITH c90 \u00a723",
            "lastName":"90\/23\/F"
            },
            {
            "firstName":"LICENSE SUSPENDED, OP MV WITH c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"LICENSE SUSPENDED, OP MV WITH c90 \u00a723",
            "lastName":"90\/23\/D"
            },
            {
            "firstName":"LICENSE SUSPENDED, OP MV WITH, CRIM SUBSQ.OFF c90 \u00a723",
            "lastName":"90\/23\/K"
            },
            {
            "firstName":"LICENSE SUSPENDED, OP MV WITH, SUBSQ.OFF c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"LICENSE SUSPENDED, OP MV WITH, SUBSQ.OFF c90 \u00a723",
            "lastName":"90\/23\/E"
            },
            {
            "firstName":"LICENSE UNDER c.131, ALTER\/FORGE c131 \u00a733",
            "lastName":"131\/33\/B"
            },
            {
            "firstName":"LICENSE, ALLOW ANOTHER TO USE c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"LICENSE, ALLOW ANOTHER TO USE c90 \u00a724(2)(a)",
            "lastName":"90\/24\/D"
            },
            {
            "firstName":"LICENSE, EXHIBIT ANOTHER'S c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"LICENSE, EXHIBIT ANOTHER'S c90 \u00a723",
            "lastName":"90\/23\/A"
            },
            {
            "firstName":"LICENSE, EXHIBIT ANOTHER'S, SUBSQ. OFF. c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"LICENSE, EXHIBIT ANOTHER'S, SUBSQ.OFF. c90 \u00a723",
            "lastName":"90\/23\/B"
            },
            {
            "firstName":"LICENSE, FALSE APPLICATION FOR MV c. 90 s. 24B",
            "lastName":"90.24B"
            },
            {
            "firstName":"LICENSE, FALSE APPLICATION FOR MV c90 \u00a724B",
            "lastName":"90\/24B\/A"
            },
            {
            "firstName":"LICENSE, FALSE STATEMENT IN APPLIC FOR c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"LICENSE, FALSE STATEMENT IN APPLIC FOR c90 \u00a724(2)(a)",
            "lastName":"90\/24\/S"
            },
            {
            "firstName":"LICENSE, REFUSE PRODUCE IN COURT c90 \u00a725",
            "lastName":"90\/25\/E"
            },
            {
            "firstName":"LICENSE\/REGIS\/PLATES, REFUSE PRODUCE c90 \u00a725",
            "lastName":"90\/25\/B"
            },
            {
            "firstName":"LIGHTS OR HEADLIGHTS, OPERATING WITHOUT c. 90 s. 7",
            "lastName":"c. 90 s. 7"
            },
            {
            "firstName":"LIGHTS VIOLATION * c85 \u00a715",
            "lastName":"85\/15\/A"
            },
            {
            "firstName":"LIGHTS VIOLATION BY NON-MOTOR VEHICLE c85 \u00a715",
            "lastName":"85\/15\/B"
            },
            {
            "firstName":"LIGHTS VIOLATION, MV * c90 \u00a77",
            "lastName":"90\/7\/C"
            },
            {
            "firstName":"LIGHTS VIOLATION, WINDSHIELD WIPERS NOT OPER c85 \u00a715",
            "lastName":"85\/15\/C"
            },
            {
            "firstName":"LIQ, MINOR TRNSPRT\/CARRY",
            "lastName":"138\/34C"
            },
            {
            "firstName":"LIQUOR CLUB, UNLICENSED c. 138 s. 61",
            "lastName":"138.61"
            },
            {
            "firstName":"LIQUOR CLUB, UNLICENSED c138 \u00a761",
            "lastName":"138\/61"
            },
            {
            "firstName":"LIQUOR ID CARD\/LICENSE, FALSE\/MISUSE c. 138 s. 34B",
            "lastName":"138.34B"
            },
            {
            "firstName":"LIQUOR ID CARD\/LICENSE, FALSE\/MISUSE c138 \u00a734B",
            "lastName":"138\/34B"
            },
            {
            "firstName":"LIQUOR INSPECTOR, OBSTRUCT c138 \u00a763A",
            "lastName":"138\/63A"
            },
            {
            "firstName":"LIQUOR LICENSING AUTH, REFUSE ID SELF TO c138 \u00a734B",
            "lastName":"138\/34B\/B"
            },
            {
            "firstName":"LIQUOR SALESPERSON WITHOUT PERMIT c. 138 s. 19A",
            "lastName":"138.19A"
            },
            {
            "firstName":"LIQUOR TO PERSON UNDER 21, SELL\/DELIVER c. 138 s. 34",
            "lastName":"138.34"
            },
            {
            "firstName":"LIQUOR TO PERSON UNDER 21, SELL\/DELIVER c138 \u00a734",
            "lastName":"138\/34"
            },
            {
            "firstName":"LIQUOR VIOLATION c138 \u00a762",
            "lastName":"138\/62"
            },
            {
            "firstName":"LIQUOR, ADULTERATE c138 \u00a716",
            "lastName":"138\/16"
            },
            {
            "firstName":"LIQUOR, ASSIST PERSON UNDER 21 PURCHASE c138 \u00a734A",
            "lastName":"138\/34A\/A"
            },
            {
            "firstName":"LIQUOR, PEDDLE FROM VEHICLE c. 138 s. 32",
            "lastName":"138.32"
            },
            {
            "firstName":"LIQUOR, PEDDLE FROM VEHICLE c138 \u00a732",
            "lastName":"138\/32"
            },
            {
            "firstName":"LIQUOR, PERSON UNDER 21 ATTEMPT PROCURE c138 \u00a734A",
            "lastName":"138\/34A\/B"
            },
            {
            "firstName":"LIQUOR, PERSON UNDER 21 POSSESS c138 \u00a734C",
            "lastName":"138\/34C\/A"
            },
            {
            "firstName":"LIQUOR, PERSON UNDER 21 POSSESS, SUBSQ. c138 \u00a734C",
            "lastName":"138\/34C\/B"
            },
            {
            "firstName":"LIQUOR, PERSON UNDER 21 PROCURE c138 \u00a734A",
            "lastName":"138\/34A\/C"
            },
            {
            "firstName":"LIQUOR, SELL\/MAKE\/STORE\/TRANSPORT UNLAW c. 138 s. 2",
            "lastName":"138.2"
            },
            {
            "firstName":"LIQUOR, SELL\/MAKE\/STORE\/TRANSPORT UNLAW c138 \u00a72",
            "lastName":"138\/2"
            },
            {
            "firstName":"LIQUOR, TRANSPORT UNLAWFULLY c. 138 s. 22",
            "lastName":"138.22"
            },
            {
            "firstName":"LIQUOR, TRANSPORT UNLAWFULLY c138 \u00a722",
            "lastName":"138\/22"
            },
            {
            "firstName":"LOAD UNSECURED\/UNCOVERED * c85 \u00a736",
            "lastName":"85\/36"
            },
            {
            "firstName":"LOBSTER CONTAINER IMPROP MARKED c130 \u00a747",
            "lastName":"130\/47\/B"
            },
            {
            "firstName":"LOBSTER, SHORT c130 \u00a744",
            "lastName":"130\/44\/B"
            },
            {
            "firstName":"LOBSTER, SHORT, SUBSQ. OFF. c. 130 s. 44",
            "lastName":"130.44"
            },
            {
            "firstName":"LOBSTER, SHORT, SUBSQ. OFF. c130 \u00a744",
            "lastName":"130\/44\/C"
            },
            {
            "firstName":"LOBSTER, TAKE EGG-BEARING c130 \u00a741",
            "lastName":"130\/41\/B"
            },
            {
            "firstName":"LOBSTER, TAKE EGG-REMOVED c130 \u00a741A",
            "lastName":"130\/41A\/B"
            },
            {
            "firstName":"LOBSTER\/CRAB LICENSE, FAIL EXHIBIT c130 \u00a738",
            "lastName":"130\/38\/B"
            },
            {
            "firstName":"LOBSTER\/CRAB VIOLATION c. 130 s. 38",
            "lastName":"130.38"
            },
            {
            "firstName":"LOBSTER\/CRAB VIOLATION c130 \u00a738",
            "lastName":"130\/38\/C"
            },
            {
            "firstName":"LOBSTER\/CRAB VIOLATION c130 \u00a738A",
            "lastName":"130\/38A\/B"
            },
            {
            "firstName":"LOBSTER\/CRAB WITHOUT LICENSE c130 \u00a737 & \u00a738",
            "lastName":"130\/37\/B"
            },
            {
            "firstName":"LOBSTER\/CRAB\/FISH POT\/CATCH, TAKE\/INJURE c130 \u00a731",
            "lastName":"130\/31"
            },
            {
            "firstName":"LODGING HOUSE, UNLICENSED c. 140 s. 24",
            "lastName":"140.24"
            },
            {
            "firstName":"LODGING HOUSE, UNLICENSED c140 \u00a724",
            "lastName":"140\/24"
            },
            {
            "firstName":"LOGAN\u00bfCARRIER $100 VIOLATION * 740 CMR \u00a723.02",
            "lastName":"740CMR2302"
            },
            {
            "firstName":"LOGAN\u00bfCARRIER $50 VIOLATION * 740 CMR \u00a723.03",
            "lastName":"740CMR2303\/A"
            },
            {
            "firstName":"LOGAN\u00bfCARRIER $50 VIOLATION * 740 CMR \u00a723.04",
            "lastName":"740CMR2304"
            },
            {
            "firstName":"LOGAN\u00bfCARRIER $50\/$100\/$200 VIOLATION * 740 CMR \u00a723.03",
            "lastName":"740CMR2303\/B"
            },
            {
            "firstName":"LOGAN\u00bfCARRIER VIOLATION * 740 CMR \u00a721.53",
            "lastName":"740CMR2153"
            },
            {
            "firstName":"LOGAN\u00bfSIGNAL\/SIGN\/MARKINGS VIOLATION * 740 CMR \u00a721.52",
            "lastName":"740CMR2152"
            },
            {
            "firstName":"LOGAN\u00bfSPEEDING OVER POSTED LIMIT * 740 CMR \u00a721.51",
            "lastName":"740CMR2151\/A"
            },
            {
            "firstName":"LOGAN\u00bfTRAFFIC VIOLATION * 740 CMR \u00a721.51",
            "lastName":"740CMR2151\/B"
            },
            {
            "firstName":"LOTTERY TICKET, ALTER\/FORGE\/COUNTERFEIT c10 \u00a730",
            "lastName":"10\/30\/A"
            },
            {
            "firstName":"LOTTERY TICKET, ALTER\/FORGE\/COUNTERFEIT\/UTTER OR PASS FALSE c. 10 s. 30",
            "lastName":"10.3"
            },
            {
            "firstName":"LOTTERY TICKET, UTTER OR PASS FALSE c10 \u00a730",
            "lastName":"10\/30\/B"
            },
            {
            "firstName":"LOTTERY, ADVERTISE OR SOLICIT FOR c. 271 s. 11",
            "lastName":"271.11"
            },
            {
            "firstName":"LOTTERY, AID FOREIGN c. 271 s. 15",
            "lastName":"271.15"
            },
            {
            "firstName":"LOTTERY, AID FOREIGN c271 \u00a715",
            "lastName":"271\/15\/A"
            },
            {
            "firstName":"LOTTERY, SELL TICKETS FOR c. 271 s. 9",
            "lastName":"271.9"
            },
            {
            "firstName":"LOTTERY, SELL TICKETS FOR c271 \u00a79",
            "lastName":"271\/9\/A"
            },
            {
            "firstName":"LOTTERY, SET UP\/PROMOTE c. 271 s. 7",
            "lastName":"271.7"
            },
            {
            "firstName":"LOTTERY, SET UP\/PROMOTE c271 \u00a77",
            "lastName":"271\/7\/A"
            },
            {
            "firstName":"LOTTERY, SET UP\/PROMOTE, SUBSQ. OFF. c. 271 s. 7",
            "lastName":"271.7"
            },
            {
            "firstName":"LOTTERY, SET UP\/PROMOTE, SUBSQ.OFF. c271 \u00a77",
            "lastName":"271\/7\/B"
            },
            {
            "firstName":"MACHINE GUN, POSSESS c269 \u00a710(c)",
            "lastName":"269\/10\/N"
            },
            {
            "firstName":"MACHINE GUN, POSSESS, 2ND OFF. c269 \u00a710(c) & (d)",
            "lastName":"269\/10\/O"
            },
            {
            "firstName":"MACHINE GUN\/SAWED-OFF SHOTGUN POSSESS, 2ND OFF. c. 269 s. 10(d)",
            "lastName":"269.10(d)"
            },
            {
            "firstName":"MACHINE GUN\/SAWED-OFF SHOTGUN, POSSESS c. 269 s. 10(c)",
            "lastName":"269.10(c)"
            },
            {
            "firstName":"MACHINERY ID NO., REMOVE\/ALTER c. 266 s. 139A",
            "lastName":"266.139A"
            },
            {
            "firstName":"MACHINERY ID NO., REMOVE\/ALTER c266 \u00a7139A",
            "lastName":"266\/139A\/A"
            },
            {
            "firstName":"MACHINERY ID NO., SELL WITH DEFACED c266 \u00a7139A",
            "lastName":"266\/139A\/B"
            },
            {
            "firstName":"MAL DESTR PROP OVER $250",
            "lastName":"266\/127"
            },
            {
            "firstName":"MANSLAUGHTER c. 265 s. 13 ",
            "lastName":"265.13"
            },
            {
            "firstName":"MANSLAUGHTER c265 \u00a713",
            "lastName":"265\/13\/A"
            },
            {
            "firstName":"MANSLAUGHTER INVOLVING EXPLOSIVES c265 \u00a713",
            "lastName":"265\/13\/B"
            },
            {
            "firstName":"MARIHUANA, POSSESS c94C \u00a734",
            "lastName":"94C\/34\/L"
            },
            {
            "firstName":"MARIHUANA, POSSESS, SUBSQ.OFF. c94C \u00a734",
            "lastName":"94C\/34\/M"
            },
            {
            "firstName":"MARIHUANA, TRAFFICKING IN  c94C \u00a732E(a)",
            "lastName":"94C\/32E\/C"
            },
            {
            "firstName":"MARIHUANA, TRAFFICKING IN c94C \u00a732E(a)",
            "lastName":"94C\/32E\/C"
            },
            {
            "firstName":"MARIJUANA, POSSESS c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"MARIJUANA, POSSESS, SUBSQ. OFF. c. 94C s. 34",
            "lastName":"94C.34"
            },
            {
            "firstName":"MARIJUANA, TRAFFICK IN c. 94C s. 32E(a)(3) - 2,000 to 10,000 lbs",
            "lastName":"94C.32E(a)(3)"
            },
            {
            "firstName":"MARIJUANA, TRAFFICK IN c. 94C s. 32E(a)(4) - 10,000 or more lbs",
            "lastName":"94C.32E(a)(4)"
            },
            {
            "firstName":"MARIJUANA, TRAFFICKING IN c. 94C s. 32E(a)(1) - 50 to 100 lbs",
            "lastName":"94C.32E(a)(1)"
            },
            {
            "firstName":"MARIJUANA, TRAFFICKING IN c. 94C s. 32E(a)(2) - 100 to 2,000 lbs",
            "lastName":"94C.32E(a)(2)"
            },
            {
            "firstName":"MARINE FISH\u00bf1971 COMPILATION VIOL 322 CMR \u00a73.00",
            "lastName":"322CMR300\/B"
            },
            {
            "firstName":"MARINE FISH\u00bfCOASTAL FISH VIOLATION 322 CMR \u00a78.00",
            "lastName":"322CMR800\/B"
            },
            {
            "firstName":"MARINE FISH\u00bfREGUL OF CATCHES VIOL 322 CMR \u00a76.00",
            "lastName":"322CMR600\/B"
            },
            {
            "firstName":"MARINE FISH\u00bfSTRIPED BASS VIOL 322 CMR \u00a76.07",
            "lastName":"322CMR607\/B"
            },
            {
            "firstName":"MARKED LANES VIOLATION * c89 \u00a74A",
            "lastName":"89\/4A"
            },
            {
            "firstName":"MARRIAGE, ABDUCT PERSON -16 FOR SECRET c. 272 s. 1",
            "lastName":"272.1"
            },
            {
            "firstName":"MARRIAGE, ABDUCT PERSON -16 FOR SECRET c272 \u00a71",
            "lastName":"272\/1"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfBRAKE VIOLATION * 730 CMR \u00a74.06",
            "lastName":"730CMR406"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfCLOSER THAN 500 FT * 730 CMR \u00a74.19",
            "lastName":"730CMR419"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfCOUPLING VIOLATION * 730 CMR \u00a74.12",
            "lastName":"730CMR412"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfDISPLAY LENGTH\/WT * 730 CMR \u00a74.11",
            "lastName":"730CMR411"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfEMERGENCY EQUIP VIOL * 730 CMR \u00a74.08",
            "lastName":"730CMR408"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfEQUIPMENT INSPECTION * 730 CMR \u00a74.15",
            "lastName":"730CMR415"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfLENGTH VIOLATION * 730 CMR \u00a74.01",
            "lastName":"730CMR401"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfPASSING VIOLATION * 730 CMR \u00a74.20",
            "lastName":"730CMR420"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfSPEEDING * 730 CMR \u00a74.18",
            "lastName":"730CMR418"
            },
            {
            "firstName":"MASS PIKE TANDEM\u00bfWEIGHT VIOLATION * 730 CMR \u00a74.02",
            "lastName":"730CMR402"
            },
            {
            "firstName":"MASS PIKE\u00bf$100 VIOLATION * 730 CMR \u00a75.04",
            "lastName":"730CMR504\/B"
            },
            {
            "firstName":"MASS PIKE\u00bf$15 VIOLATION * 730 CMR \u00a75.04",
            "lastName":"730CMR504\/E"
            },
            {
            "firstName":"MASS PIKE\u00bf$500 VIOLATION * 730 CMR \u00a75.04",
            "lastName":"730CMR504\/A"
            },
            {
            "firstName":"MASS PIKE\u00bfBRAKES VIOLATION * 730 CMR \u00a77.05(5)(g)",
            "lastName":"730CMR705\/D"
            },
            {
            "firstName":"MASS PIKE\u00bfBREAKDOWN LANE VIOLATION *  730 CMR \u00a77.08(9)",
            "lastName":"730CMR708\/A"
            },
            {
            "firstName":"MASS PIKE\u00bfCOASTING VIOLATION *  730 CMR \u00a77.08(16)",
            "lastName":"730CMR708\/B"
            },
            {
            "firstName":"MASS PIKE\u00bfCOMMERCIAL ACTIVITY  730 CMR \u00a77.05(9)",
            "lastName":"730CMR705\/E"
            },
            {
            "firstName":"MASS PIKE\u00bfCOMMON CARRIER FL STOP FOR POLICE *  730 CMR \u00a77.08(30)",
            "lastName":"730CMR708\/C"
            },
            {
            "firstName":"MASS PIKE\u00bfCROSS-OVER VIOLATION *  730 CMR \u00a77.08(10)(b)",
            "lastName":"730CMR708\/E"
            },
            {
            "firstName":"MASS PIKE\u00bfDISABLED VEH REPAIR\/TOW VIOL *  730 CMR \u00a77.11",
            "lastName":"730CMR711"
            },
            {
            "firstName":"MASS PIKE\u00bfDUTY STATUS RECORD VIOLATION *  730 CMR \u00a77.08(32)",
            "lastName":"730CMR708\/G"
            },
            {
            "firstName":"MASS PIKE\u00bfENTER\/EXIT IMPROPERLY * 730 CMR \u00a77.08(7)",
            "lastName":"730CMR708\/H"
            },
            {
            "firstName":"MASS PIKE\u00bfENTER\/EXIT, UNAUTHORIZED * 730 CMR \u00a77.05(3)",
            "lastName":"730CMR705\/G"
            },
            {
            "firstName":"MASS PIKE\u00bfEQUIPMENT VIOLATON *  730 CMR \u00a77.08(27)",
            "lastName":"730CMR708\/J"
            },
            {
            "firstName":"MASS PIKE\u00bfETC SYSTEM\/LANE, UNAUTH USE * 730 CMR \u00a77.04(1)",
            "lastName":"730CMR704\/A"
            },
            {
            "firstName":"MASS PIKE\u00bfETC TOLL, AVOID * 730 CMR \u00a77.04(3)",
            "lastName":"730CMR704\/B"
            },
            {
            "firstName":"MASS PIKE\u00bfEXCLUDED AREA IN CONSTRUCTION ZONE * 730 CMR \u00a77.08(12)(b)",
            "lastName":"730CMR708\/K"
            },
            {
            "firstName":"MASS PIKE\u00bfEXPLOSIVES PERMIT, FAIL CARRY *  730 CMR \u00a77.06(5)(f)(2)",
            "lastName":"730CMR706\/A"
            },
            {
            "firstName":"MASS PIKE\u00bfFUEL, INADEQUATE *  730 CMR \u00a77.08(23)",
            "lastName":"730CMR708\/L"
            },
            {
            "firstName":"MASS PIKE\u00bfHAZARDOUS MATERIAL VIOLATION * 730 CMR \u00a77.10",
            "lastName":"730CMR710"
            },
            {
            "firstName":"MASS PIKE\u00bfHAZARDOUS MATERIAL W\/O PERMIT * 730 CMR \u00a77.05(5)(m)",
            "lastName":"730CMR705\/K"
            },
            {
            "firstName":"MASS PIKE\u00bfHEADLIGHT HIGH BEAM VIOLATION *  730 CMR \u00a77.08(22)",
            "lastName":"730CMR708\/M"
            },
            {
            "firstName":"MASS PIKE\u00bfHEIGHT CLEARANCE, FAIL CHECK *  730 CMR \u00a77.06(4)(g)",
            "lastName":"730CMR706\/E"
            },
            {
            "firstName":"MASS PIKE\u00bfHEIGHT WARNING SIGNAL, IGNORE *  730 CMR \u00a77.08(19)",
            "lastName":"730CMR708\/N"
            },
            {
            "firstName":"MASS PIKE\u00bfHEIGHT, FAIL DISPLAY *  730 CMR \u00a77.06(4)(f)",
            "lastName":"730CMR706\/F"
            },
            {
            "firstName":"MASS PIKE\u00bfIDLING *  730 CMR \u00a77.08(28)",
            "lastName":"730CMR708\/P"
            },
            {
            "firstName":"MASS PIKE\u00bfINSPECTION STICKER, NO *   730 CMR \u00a77.08(26)",
            "lastName":"730CMR708\/Q"
            },
            {
            "firstName":"MASS PIKE\u00bfLEFT LANE RESTRICTION * 730 CMR \u00a77.08(11)(b)",
            "lastName":"730CMR708\/R"
            },
            {
            "firstName":"MASS PIKE\u00bfLIQUOR, UNLAWFULLY TRANSPORT *  730 CMR \u00a77.08(29)",
            "lastName":"730CMR708\/S"
            },
            {
            "firstName":"MASS PIKE\u00bfLOADING, NEGLIGENT * 730 CMR \u00a77.08(5)(b)",
            "lastName":"730CMR708\/T"
            },
            {
            "firstName":"MASS PIKE\u00bfLOITERING  730 CMR \u00a77.05(8)",
            "lastName":"730CMR705\/M"
            },
            {
            "firstName":"MASS PIKE\u00bfMARKED LANES VIOLATION *  700 CMR \u00a77.09(5)(a)",
            "lastName":"700CMR709\/U"
            },
            {
            "firstName":"MASS PIKE\u00bfMARKED LANES VIOLATION *  730 CMR \u00a77.08(8)",
            "lastName":"730CMR708\/U"
            },
            {
            "firstName":"MASS PIKE\u00bfMEDIAN\/EXCLUDED AREA VIOLATION * 730 CMR \u00a77.08(10)(a)",
            "lastName":"730CMR708\/V"
            },
            {
            "firstName":"MASS PIKE\u00bfMINIMUM SPEED VIOLATION * 730 CMR \u00a77.08(6)(c)",
            "lastName":"730CMR708\/W"
            },
            {
            "firstName":"MASS PIKE\u00bfMOTOR CARRIER SAFETY ACT VIOL * 730 CMR \u00a77.09",
            "lastName":"730CMR709"
            },
            {
            "firstName":"MASS PIKE\u00bfNEGLIGENT OP IN CONSTRUCTION ZONE *  730 CMR \u00a77.08(12)(c)",
            "lastName":"730CMR708\/Z"
            },
            {
            "firstName":"MASS PIKE\u00bfNEGLIGENT OPERATION *  700 CMR \u00a77.09(5)(a)",
            "lastName":"700CMR709\/Y"
            },
            {
            "firstName":"MASS PIKE\u00bfNEGLIGENT OPERATION * 730 CMR \u00a77.08(5)(a)",
            "lastName":"730CMR708\/Y"
            },
            {
            "firstName":"MASS PIKE\u00bfNOISE VIOLATION *  730 CMR \u00a77.08(21)",
            "lastName":"730CMR708\/AA"
            },
            {
            "firstName":"MASS PIKE\u00bfPASSING VIOLATION *  730 CMR \u00a77.08(14)",
            "lastName":"730CMR708\/FF"
            },
            {
            "firstName":"MASS PIKE\u00bfPEDESTRIAN 730 CMR \u00a75.04(4)(b)",
            "lastName":"730CMR504\/Q"
            },
            {
            "firstName":"MASS PIKE\u00bfPILOT CAR VIOLATION *  730 CMR \u00a77.06(4)(d)",
            "lastName":"730CMR706\/J"
            },
            {
            "firstName":"MASS PIKE\u00bfPOLICE ORDERS, FAIL OBEY *  730 CMR \u00a77.08(1)(b)",
            "lastName":"730CMR708\/GG"
            },
            {
            "firstName":"MASS PIKE\u00bfRESTRICTED AREA VIOLATION *  730 CMR \u00a77.08(11)(a)",
            "lastName":"730CMR708\/JJ"
            },
            {
            "firstName":"MASS PIKE\u00bfRIGHT LANE, FAIL KEEP TO *  730 CMR \u00a77.08(13)",
            "lastName":"730CMR708\/KK"
            },
            {
            "firstName":"MASS PIKE\u00bfSIGN, FAIL OBEY * 730 CMR \u00a77.08(1)(a)",
            "lastName":"730CMR708\/LL"
            },
            {
            "firstName":"MASS PIKE\u00bfSIGN\/SIGNAL\/MARKING, UNAUTHORIZED 730 CMR \u00a77.08(1)(a)",
            "lastName":"730CMR708\/NN"
            },
            {
            "firstName":"MASS PIKE\u00bfSIGNAL\/SIGN\/MARKINGS, UNAUTH 730 CMR \u00a75.04(1)(b)",
            "lastName":"730CMR504\/S"
            },
            {
            "firstName":"MASS PIKE\u00bfSIGNAL\/SIGN\/MARKINGS,VANDALIZE 730 CMR \u00a75.04(1)(d)",
            "lastName":"730CMR504\/T"
            },
            {
            "firstName":"MASS PIKE\u00bfSOLICIT FUNDS  730 CMR \u00a77.05(9)",
            "lastName":"730CMR705\/T"
            },
            {
            "firstName":"MASS PIKE\u00bfSOLICITING 730 CMR \u00a75.04(4)(g)",
            "lastName":"730CMR504\/K"
            },
            {
            "firstName":"MASS PIKE\u00bfSPECIAL FUEL PERMIT, FAIL CARRY * 730 CMR \u00a77.06(6)(e)(2)",
            "lastName":"730CMR706\/M"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING * 730 CMR \u00a75.04",
            "lastName":"730CMR504\/F"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING * 730 CMR \u00a77.08(6)(a)",
            "lastName":"730CMR708\/PP"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING IN CONSTRUCTION ZONE *  730 CMR \u00a77.08(12)(a)",
            "lastName":"730CMR708\/QQ"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING OVER POSTED LIMIT *  700 CMR \u00a77.09(6)(c)",
            "lastName":"700CMR709\/RR"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING OVER POSTED LIMIT *  730 CMR \u00a77.08(6)(c)",
            "lastName":"730CMR708\/RR"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING OVER POSTED LIMIT * 730 CMR \u00a75.04",
            "lastName":"730CMR504\/G"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING TO ENDANGER *  700 CMR \u00a77.09(6)(b)",
            "lastName":"700CMR709\/SS"
            },
            {
            "firstName":"MASS PIKE\u00bfSPEEDING TO ENDANGER *  730 CMR \u00a77.08(6)(b)",
            "lastName":"730CMR708\/SS"
            },
            {
            "firstName":"MASS PIKE\u00bfSTOP\/BACK\/U-TURN *  730 CMR \u00a77.08(17)(a)&(b)",
            "lastName":"730CMR708\/TT"
            },
            {
            "firstName":"MASS PIKE\u00bfSTOP\/TURN, FAIL SIGNAL *  730 CMR \u00a77.08(17)(c)",
            "lastName":"730CMR708\/UU"
            },
            {
            "firstName":"MASS PIKE\u00bfTANDEM IN TUNNEL *  730 CMR \u00a77.06(2)(m)",
            "lastName":"730CMR706\/R"
            },
            {
            "firstName":"MASS PIKE\u00bfTANDEM LIGHTS VIOLATION * 730 CMR \u00a77.07(16)",
            "lastName":"730CMR707\/J"
            },
            {
            "firstName":"MASS PIKE\u00bfTANDEM PASSING VIOLATION * 730 CMR \u00a77.07(22)",
            "lastName":"730CMR707\/N"
            },
            {
            "firstName":"MASS PIKE\u00bfTANDEM TOO CLOSE * 730 CMR \u00a77.07(20)",
            "lastName":"730CMR707\/U"
            },
            {
            "firstName":"MASS PIKE\u00bfTIRE VIOLATION *  730 CMR \u00a77.05(5)(b)",
            "lastName":"730CMR705\/X"
            },
            {
            "firstName":"MASS PIKE\u00bfTOLL BOOTH, FAIL STOP AT *  730 CMR \u00a77.03(2)",
            "lastName":"730CMR703\/A"
            },
            {
            "firstName":"MASS PIKE\u00bfTOLL, EVADE *  730 CMR \u00a77.03(4)",
            "lastName":"730CMR703\/B"
            },
            {
            "firstName":"MASS PIKE\u00bfTOLL, FAIL PAY *  730 CMR \u00a77.03(3)",
            "lastName":"730CMR703\/C"
            },
            {
            "firstName":"MASS PIKE\u00bfTOO CLOSE *  700 CMR \u00a77.09(15)",
            "lastName":"700CMR709\/VV"
            },
            {
            "firstName":"MASS PIKE\u00bfTOO CLOSE *  730 CMR \u00a77.08(15)",
            "lastName":"730CMR708\/VV"
            },
            {
            "firstName":"MASS PIKE\u00bfTRAFFIC LIGHT, FAIL OBEY * 730 CMR \u00a77.08(2)",
            "lastName":"730CMR708\/WW"
            },
            {
            "firstName":"MASS PIKE\u00bfTRASH, IMPROP DISPOSE OF MINOR  730 CMR \u00a77.08(24)(a)",
            "lastName":"730CMR708\/XX"
            },
            {
            "firstName":"MASS PIKE\u00bfWEIGHT VIOLATION * 730 CMR \u00a75.04",
            "lastName":"730CMR504\/H"
            },
            {
            "firstName":"MASS PIKE\u00bfWEIGHT VIOLATION * 730 CMR \u00a77.05(5)(h)",
            "lastName":"730CMR705\/Z"
            },
            {
            "firstName":"MASS PIKE\u00bfWRONG WAY * 730 CMR \u00a77.05(1)",
            "lastName":"730CMR705\/CC"
            },
            {
            "firstName":"MASS PIKE\u00bfWRONG WAY IN TUNNEL *  730 CMR \u00a77.05(2)",
            "lastName":"730CMR705\/DD"
            },
            {
            "firstName":"MASSACHUSETTS STATE COLLEGE BUILDING AUTHORITY, FINANCIAL INTEREST VIOLATION c. 73 App. s. 1-2",
            "lastName":"73 App..1-2"
            },
            {
            "firstName":"MASSAGE\/BATHS, UNLICENSED c140 \u00a751",
            "lastName":"140\/51"
            },
            {
            "firstName":"MASSPORT\u00bfSPEEDING OVER POSTED LIMIT * 740 CMR \u00a73.03",
            "lastName":"740CMR303\/A"
            },
            {
            "firstName":"MASTER\/ARBITRATOR\/REFEREE, ATT TO BRIBE c268 \u00a713",
            "lastName":"268\/13\/D"
            },
            {
            "firstName":"MAYFLOWER PLANT, TAKE\/INJURE c2 \u00a77",
            "lastName":"2\/7\/A"
            },
            {
            "firstName":"MAYHEM c. 265 s. 14",
            "lastName":"265.14"
            },
            {
            "firstName":"MAYHEM c265 \u00a714",
            "lastName":"265\/14\/A"
            },
            {
            "firstName":"MBOAT EQUIPMENT VIOL BY LESSOR c90B \u00a77",
            "lastName":"90B\/7\/B"
            },
            {
            "firstName":"MBOAT EQUIPMENT VIOLATION 323 CMR \u00a72.06",
            "lastName":"323CMR206\/B"
            },
            {
            "firstName":"MBOAT EQUIPMENT VIOLATION c90B \u00a75",
            "lastName":"90B\/5\/B"
            },
            {
            "firstName":"MBOAT ID NO. CERTIF, FAIL POSSESS c90B \u00a73(a)",
            "lastName":"90B\/3\/B"
            },
            {
            "firstName":"MBOAT ID NO. CERTIFICATE, NO c90B \u00a73(a)",
            "lastName":"90B\/3\/D"
            },
            {
            "firstName":"MBOAT ID NO., DISPLAY WRONG c90B \u00a73(j)",
            "lastName":"90B\/3\/F"
            },
            {
            "firstName":"MBOAT ID NO., FAIL DISPLAY c90B \u00a73(a)",
            "lastName":"90B\/3\/H"
            },
            {
            "firstName":"MBOAT ID NO., OPERATE WITHOUT c90B \u00a72",
            "lastName":"90B\/2\/B"
            },
            {
            "firstName":"MBOAT ID NO., VIOLATIONS c. 90B s. 4B",
            "lastName":"90B.4B"
            },
            {
            "firstName":"MBOAT MANUFACTURER ID NO., REMOVE c90B \u00a74B",
            "lastName":"90B\/4B\/C"
            },
            {
            "firstName":"MBOAT OPERATION VIOLATION 323 CMR \u00a72.07",
            "lastName":"323CMR207\/B"
            },
            {
            "firstName":"MBOAT REFUSE STOP\/ID FOR OFFICER c90B \u00a712",
            "lastName":"90B\/12\/B"
            },
            {
            "firstName":"MBOAT, VIOLATION OF REGULATIONS c. 90B s. 14(c)",
            "lastName":"90B.14(c)"
            },
            {
            "firstName":"MBTA FARE, ATTEMPT TO EVADE c159 \u00a7101",
            "lastName":"159\/101\/A"
            },
            {
            "firstName":"MBTA FARE, EVADE c159 \u00a7101",
            "lastName":"159\/101\/B"
            },
            {
            "firstName":"MBTA PASS, STOLEN\/COUNTERFEIT c161 \u00a7113A",
            "lastName":"161\/113A"
            },
            {
            "firstName":"MBTA, POSSESS LIQUOR TO CONSUME ON c. 161A s. 5",
            "lastName":"161A.5"
            },
            {
            "firstName":"MBTA, POSSESS LIQUOR TO CONSUME ON c161A \u00a75",
            "lastName":"161A\/5"
            },
            {
            "firstName":"MDC RESERVATIONS\/HWAYS REGULATIONS VIOL c92 \u00a737",
            "lastName":"92\/37"
            },
            {
            "firstName":"MDC WATERSHED\u00bfMV VIOLATION  350 CMR \u00a711.09",
            "lastName":"350CMR1109\/A"
            },
            {
            "firstName":"MDC WATERSHED\u00bfNON-MV VIOLATION 350 CMR \u00a711.09",
            "lastName":"350CMR1109\/B"
            },
            {
            "firstName":"MDC WAY\u00bf$100 VIOLATION * 350 CMR \u00a74.01",
            "lastName":"350CMR401\/B"
            },
            {
            "firstName":"MDC WAY\u00bf$200 VIOLATION * 350 CMR \u00a74.01",
            "lastName":"350CMR401\/A"
            },
            {
            "firstName":"MDC WAY\u00bf$25 VIOLATION * 350 CMR \u00a74.01",
            "lastName":"350CMR401\/D"
            },
            {
            "firstName":"MDC WAY\u00bf$50 VIOLATION * 350 CMR \u00a74.01",
            "lastName":"350CMR401\/C"
            },
            {
            "firstName":"MDC WAY\u00bfSOLICITING FROM PERSONS IN MVS 350 CMR \u00a74.01",
            "lastName":"350CMR401\/I"
            },
            {
            "firstName":"MDC WAY\u00bfSPEEDING * 350 CMR \u00a74.01",
            "lastName":"350CMR401\/E"
            },
            {
            "firstName":"MDC WAY\/RESERV\u00bfENTRY\/EXIT, IMPROPER MV * 350 CMR \u00a72.01(2)",
            "lastName":"350CMR201\/A"
            },
            {
            "firstName":"MDC WAY\/RESERV\u00bfNON-MV VIOLATION 350 CMR \u00a72.01(2)",
            "lastName":"350CMR201\/B"
            },
            {
            "firstName":"MDC WAY\/RESERV\u00bfTRASH VIOL 350 CMR \u00a72.01(2)(r) or (s)",
            "lastName":"350CMR201\/C"
            },
            {
            "firstName":"MDC\u00bfCHARLES RIVER BASIN VIOLATION 350 CMR \u00a712.02",
            "lastName":"350CMR1202"
            },
            {
            "firstName":"MEDICAL ASSISTANCE FRAUD BY NON-PROVIDER c. 118E s. 40",
            "lastName":"118E.40"
            },
            {
            "firstName":"MEDICAL ASSISTANCE FRAUD BY NON-PROVIDER c118E \u00a740",
            "lastName":"118E\/40\/A"
            },
            {
            "firstName":"MEDICAL ASSISTANCE FRAUD BY PROVIDER c118E \u00a740",
            "lastName":"118E\/40\/B"
            },
            {
            "firstName":"MEDICAL ASSISTANCE, FALSE STATEMENT FOR c. 118E s. 39",
            "lastName":"118E.39"
            },
            {
            "firstName":"MEDICAL ASSISTANCE, FALSE STATEMENT FOR c118E \u00a739",
            "lastName":"118E\/39"
            },
            {
            "firstName":"MEDICAL FACILITY, OBSTRUCT c. 266 s. 120E",
            "lastName":"266.120E"
            },
            {
            "firstName":"MEDICAL FACILITY, OBSTRUCT c266 \u00a7120E",
            "lastName":"266\/120E\/A"
            },
            {
            "firstName":"MEDICAL LICENSE, FRAUDULENT APPLIC FOR c112 \u00a76",
            "lastName":"112\/6\/C"
            },
            {
            "firstName":"MEDICINE, UNAUTHORIZED PRACTICE OF c112 \u00a76",
            "lastName":"112\/6\/A"
            },
            {
            "firstName":"METHAMPHETAMINE (c.94C s. 31, Class B(c)(2)), DISTRIBUTE OR POSSESS WITH INTENT c. 94C s. 32A(c)",
            "lastName":"94C.32A(c)"
            },
            {
            "firstName":"METHAMPHETAMINE (c.94C s. 31, Class B(c)(2)), DISTRIBUTE OR POSSESS WITH INTENT, SUBSQ. OFF. c. 94C s. 32A(d)",
            "lastName":"94C.32A(d)"
            },
            {
            "firstName":"METHAMPHETAMINE, DISTRIBUTE c94C \u00a732A(c)",
            "lastName":"94C\/32A\/I"
            },
            {
            "firstName":"METHAMPHETAMINE, DISTRIBUTE, SUBSQ.OFF. c94C \u00a732A(d)",
            "lastName":"94C\/32A\/J"
            },
            {
            "firstName":"METHAMPHETAMINE, POSSESS TO DISTRIB c94C \u00a732A(c)",
            "lastName":"94C\/32A\/K"
            },
            {
            "firstName":"METHAMPHETAMINE, POSSESS TO DISTRIB, 2ND c94C \u00a732A(d)",
            "lastName":"94C\/32A\/L"
            },
            {
            "firstName":"METHAMPHETAMINE, TRAFFICKING IN c94C \u00a732E(b)",
            "lastName":"94C\/32E\/D"
            },
            {
            "firstName":"METHAMPHETAMINE, TRAFFICKING IN, 100 GRAMS OR MORE c94C \u00a732E(b)",
            "lastName":"94C\/32E\/T"
            },
            {
            "firstName":"METHAMPHETAMINE, TRAFFICKING IN, 18 GRAMS OR MORE, LESS 36 c94C \u00a732E(c)",
            "lastName":"94C\/32E\/R"
            },
            {
            "firstName":"METHAMPHETAMINE, TRAFFICKING IN, 200 GRAMS OR MORE c94C \u00a732E(b)",
            "lastName":"94C\/32E\/U"
            },
            {
            "firstName":"METHAMPHETAMINE, TRAFFICKING IN, 36 GRAMS OR MORE, LESS 100 c94C \u00a732E(b)",
            "lastName":"94C\/32E\/S"
            },
            {
            "firstName":"MILITARY STATUS CHANGE, FAIL REPORT, 2ND c90 \u00a78",
            "lastName":"90\/8\/B"
            },
            {
            "firstName":"MILK CASE, TAKE\/CONVERT c266 \u00a7144",
            "lastName":"266\/144"
            },
            {
            "firstName":"MINIMUM WAGE COMPLAINT, WILFULLY RETALIATE FOR, 2D c151 \u00a719",
            "lastName":"151\/19\/V"
            },
            {
            "firstName":"MISCELLANEOUS CODE OF MASS REGS VIOLATN",
            "lastName":"777777"
            },
            {
            "firstName":"MISCELLANEOUS COMMON LAW VIOLATION",
            "lastName":"888888"
            },
            {
            "firstName":"MISCELLANEOUS MUNIC ORDINANCE\/BYLAW VIOL",
            "lastName":"666666"
            },
            {
            "firstName":"MISCELLANEOUS STATUTORY VIOLATION",
            "lastName":"999999"
            },
            {
            "firstName":"MOBILE PHONE, OPERATOR USE IMPOPERLY c90 \u00a713",
            "lastName":"90\/13H"
            },
            {
            "firstName":"MOLOTOV COCKTAIL, MAKE\/SELL\/USE\/POSSESS c. 266 s. 102B",
            "lastName":"266.102B"
            },
            {
            "firstName":"MOLOTOV COCKTAIL, MAKE\/SELL\/USE\/POSSESS c266 \u00a7102B",
            "lastName":"266\/102B"
            },
            {
            "firstName":"MONEY LAUNDERING c267A \u00a72",
            "lastName":"267A\/2"
            },
            {
            "firstName":"MOPED OPERATION BY UNLIC -17 c90 \u00a71B",
            "lastName":"90\/1B\/A"
            },
            {
            "firstName":"MOPED OPERATION BY UNLIC -17, 2ND OFF. c90 \u00a71B",
            "lastName":"90\/1B\/B"
            },
            {
            "firstName":"MOPED OPERATION BY UNLIC -17, 3RD OFF. c90 \u00a71B",
            "lastName":"90\/1B\/C"
            },
            {
            "firstName":"MOPED VIOLATION * c90 \u00a71B",
            "lastName":"90\/1B\/D"
            },
            {
            "firstName":"MORTGAGE BROKER OR LENDER LICENSE REQUIREMENT; VIOLATION c. 255E s. 2",
            "lastName":"255E.2"
            },
            {
            "firstName":"MORTGAGED PERSONALTY, CONCEAL c266 \u00a782",
            "lastName":"266\/82\/A"
            },
            {
            "firstName":"MORTGAGED PERSONALTY, SELL c. 266 s. 83",
            "lastName":"266.83"
            },
            {
            "firstName":"MORTGAGED\/LEASED PERSONALTY, CONCEAL, HOLD LIQUOR c. 266 s. 82",
            "lastName":"266.82"
            },
            {
            "firstName":"MOTOR CARRIER FUEL EXCISE TAX VIOLATION c. 64F s. 12",
            "lastName":"64F.12"
            },
            {
            "firstName":"MOTOR CARRIER SAFETY VIOLATION 540 CMR \u00a714.03",
            "lastName":"540CMR1403\/B"
            },
            {
            "firstName":"MOTOR VEH BY-LAW VIOLATION * c85 \u00a710",
            "lastName":"85\/10\/B"
            },
            {
            "firstName":"MOTOR VEH DOOR, NEGLIGENTLY OPEN c90 \u00a714",
            "lastName":"90\/14\/E"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE BY NEGLIGENT OP c. 90 s. 24G(b)",
            "lastName":"90.24G(b)"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE BY NEGLIGENT OP c90 \u00a724G(b)",
            "lastName":"90\/24G\/A"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE BY RECKLESS OP c. 90 s. 24G(b)",
            "lastName":"90.24G(b)"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE BY RECKLESS OP c90 \u00a724G(b)",
            "lastName":"90\/24G\/B"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI LIQUOR & NEGLIG c90 \u00a724G(a)",
            "lastName":"90\/24G\/G"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI LIQUOR OR DRUGS & NEGLIG c. 90 s. 24G(a)",
            "lastName":"90.24G(a)"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI LIQUOR OR DRUGS & RECKL c. 90 s. 24G(a)",
            "lastName":"90.24G(a)"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI LIQUOR OR DRUGS c. 90 s. 24G(b)",
            "lastName":"90.24G(b)"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI\u00bfDRUGS & NEGLIG c90 \u00a724G(a)",
            "lastName":"90\/24G\/D"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI\u00bfDRUGS & RECKLESS c90 \u00a724G(a)",
            "lastName":"90\/24G\/E"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI\u00bfDRUGS c90 \u00a724G(b)",
            "lastName":"90\/24G\/C"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI\u00bfLIQUOR & RECKL c90 \u00a724G(a)",
            "lastName":"90\/24G\/H"
            },
            {
            "firstName":"MOTOR VEH HOMICIDE OUI\u00bfLIQUOR c90 \u00a724G(b)",
            "lastName":"90\/24G\/F"
            },
            {
            "firstName":"MOTOR VEH IN AREA CLOSED TO TRAVEL * c90 \u00a718",
            "lastName":"90\/18\/B"
            },
            {
            "firstName":"MOTOR VEH IN FELONY\/LARCENY, USE c90 \u00a724A",
            "lastName":"90\/24A"
            },
            {
            "firstName":"MOTOR VEH INSPECTION STATION VIOLATION 540 CMR \u00a74.00",
            "lastName":"540CMR400"
            },
            {
            "firstName":"MOTOR VEH INSURANCE RATING VIOL c. 175E s. 2 - 12",
            "lastName":"175E.2 - 12"
            },
            {
            "firstName":"MOTOR VEH MASTER KEY, POSSESS c266 \u00a749",
            "lastName":"266\/49\/C"
            },
            {
            "firstName":"MOTOR VEH THEFT, FALSE REPORT OF c. 268 s. 39",
            "lastName":"268.39"
            },
            {
            "firstName":"MOTOR VEH THEFT, FALSE REPORT OF c268 \u00a739",
            "lastName":"268\/39\/A"
            },
            {
            "firstName":"MOTOR VEH THEFT, FALSE REPORT OF, SUBSQ. OFF. c. 268 s. 39",
            "lastName":"268.39"
            },
            {
            "firstName":"MOTOR VEH THIEF, CONCEAL c. 266 s. 28(b) ",
            "lastName":"266.28(b)"
            },
            {
            "firstName":"MOTOR VEH THIEF, CONCEAL c266 \u00a728(b)",
            "lastName":"266\/28\/A"
            },
            {
            "firstName":"MOTOR VEH TO DEFRAUD, REMOVE c. 266 s. 27A ",
            "lastName":"266.27A"
            },
            {
            "firstName":"MOTOR VEH TO DEFRAUD, REMOVE c266 \u00a727A",
            "lastName":"266\/27A\/A"
            },
            {
            "firstName":"MOTOR VEH TO DEFRAUD, REMOVE SUBSQ. OFF. c. 266 s. 27A ",
            "lastName":"266.27A"
            },
            {
            "firstName":"MOTOR VEH VIN, REMOVE\/ALTER c. 266 s. 139(a)",
            "lastName":"266.139(a)"
            },
            {
            "firstName":"MOTOR VEH VIN, REMOVE\/ALTER c266 \u00a7139(a)",
            "lastName":"266\/139\/A"
            },
            {
            "firstName":"MOTOR VEH WITH DEFACED VIN, ATT TO SELL c266 \u00a7139(b)",
            "lastName":"266\/139\/B"
            },
            {
            "firstName":"MOTOR VEH WITH DEFACED VIN, POSSESS\/RECV c. 266 s. 139(c)",
            "lastName":"266.139(c)"
            },
            {
            "firstName":"MOTOR VEH WITH DEFACED VIN, POSSESS\/RECV c266 \u00a7139(c)",
            "lastName":"266\/139\/C"
            },
            {
            "firstName":"MOTOR VEH WITH DEFACED VIN, SELL c266 \u00a7139(b)",
            "lastName":"266\/139\/D"
            },
            {
            "firstName":"MOTOR VEH WITH DEFACED VIN, SELL OR ATT TO SELL c. 266 s. 139(b)",
            "lastName":"266.139(b)"
            },
            {
            "firstName":"MOTOR VEH, LARCENY OF c266 \u00a728(a)",
            "lastName":"266\/28\/B"
            },
            {
            "firstName":"MOTOR VEH, LARCENY OF, SUBSQ.OFF. c266 \u00a728(a)",
            "lastName":"266\/28\/C"
            },
            {
            "firstName":"MOTOR VEH, LARCENY OF\/MALICIOUS DAMAGE\/RECEIVE STOLEN\/TAKE AND STEAL PARTS c. 266 s. 28(a)",
            "lastName":"266.28(a)"
            },
            {
            "firstName":"MOTOR VEH, LARCENY OF\/MALICIOUS DAMAGE\/RECEIVE STOLEN\/TAKE AND STEAL PARTS, SUBSQ. OFF. c. 266 s. 28(a)",
            "lastName":"266.28(a)"
            },
            {
            "firstName":"MOTOR VEH, MALICIOUS DAMAGE TO c266 \u00a728(a)",
            "lastName":"266\/28\/D"
            },
            {
            "firstName":"MOTOR VEH, MALICIOUS DAMAGE TO, SUBSQ OFF c266 \u00a728(a)",
            "lastName":"266\/28\/E"
            },
            {
            "firstName":"MOTOR VEH, MALICIOUS DAMAGE TO,SUBSQ.OFF c266 \u00a728(a)",
            "lastName":"266\/28\/E"
            },
            {
            "firstName":"MOTOR VEH, RECEIVE STOLEN c266 \u00a728(a)",
            "lastName":"266\/28\/F"
            },
            {
            "firstName":"MOTOR VEH, RECEIVE STOLEN, SUBSQ.OFF. c266 \u00a728(a)",
            "lastName":"266\/28\/G"
            },
            {
            "firstName":"MOTOR VEH, REMOVE IMPROPERLY c266 \u00a7120D",
            "lastName":"266\/120D"
            },
            {
            "firstName":"MOTOR VEH, TAKING & STEALING PARTS c266 \u00a728(a)",
            "lastName":"266\/28\/H"
            },
            {
            "firstName":"MOTOR VEH, TAKING & STEALING PARTS,SUBSQ. c266 \u00a728(a)",
            "lastName":"266\/28\/I"
            },
            {
            "firstName":"MOTOR VEHICLE OPERATOR FAILURE TO IDENTIFY SELF, REFUSING TO SUBMIT c. 90 s.25",
            "lastName":"c. 90 s. 25"
            },
            {
            "firstName":"MOTOR VEHICLES AND AIRCRAFT, APPEALS AND HEARINGS, SWEARS\/AFFIRMS FALSELY    c. 90 s. 28",
            "lastName":"90.28"
            },
            {
            "firstName":"MOTORCYCLE EQUIPMENT VIOLATION * c90 \u00a77",
            "lastName":"90\/7\/E"
            },
            {
            "firstName":"MOTORCYCLE PASSENGER VIOLATION * c90 \u00a77",
            "lastName":"90\/7\/F"
            },
            {
            "firstName":"MOTORCYCLE, NOISY * c90 \u00a77U",
            "lastName":"90\/7U"
            },
            {
            "firstName":"MOTORCYCLE, OPERATING WITHOUT HEADGEAR c. 90 s. 7",
            "lastName":"90.7"
            },
            {
            "firstName":"MOTORIZED SCOOTER VIOLATION c90 \u00a71E",
            "lastName":"90\/1E"
            },
            {
            "firstName":"MUNICIPAL BY-LAW OR ORDINANCE VIOLATION c40 \u00a721",
            "lastName":"40\/21\/B"
            },
            {
            "firstName":"MUNICIPAL BY-LAW VIOLATION c85 \u00a710",
            "lastName":"85\/10\/C"
            },
            {
            "firstName":"MUNICIPAL SEAL, USE WITHOUT AUTHORITY c268 \u00a735",
            "lastName":"268\/35\/A"
            },
            {
            "firstName":"MUNICIPAL\/COUNTY OFFCR, EMBEZZLEMENT BY c266 \u00a751",
            "lastName":"266\/51"
            },
            {
            "firstName":"MURDER c. 265 s. 1",
            "lastName":"265.1"
            },
            {
            "firstName":"MURDER c265 \u00a71",
            "lastName":"265\/1"
            },
            {
            "firstName":"MURDER, ATTEMPTED c. 265 s. 16",
            "lastName":"265.16"
            },
            {
            "firstName":"MURDER, ATTEMPTED c265 \u00a716",
            "lastName":"265\/16"
            },
            {
            "firstName":"MV DOC. US. FLS,STOLEN, ETC.",
            "lastName":"90\/24B"
            },
            {
            "firstName":"NAME\/ADDRESS CHANGE, FL NOTIFY RMV OF * c90 \u00a726A",
            "lastName":"90\/26A"
            },
            {
            "firstName":"NAME\/ADDRESS, MV OP REFUSE GIVE AT NT * c85 \u00a716",
            "lastName":"85\/16\/A"
            },
            {
            "firstName":"NAME\/ADDRESS, REFUSE GIVE AT NIGHT c85 \u00a716",
            "lastName":"85\/16\/B"
            },
            {
            "firstName":"NATIONAL NETWORK TRAVEL LIMITATION VIOL * 720 CMR \u00a710.02",
            "lastName":"720CMR1002"
            },
            {
            "firstName":"NEGLIGENT OPERATION OF MOTOR VEHICLE c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"NEGLIGENT OPERATION OF MOTOR VEHICLE c90 \u00a724(2)(a)",
            "lastName":"90\/24\/E"
            },
            {
            "firstName":"NIGHTWALKER, COMMON c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"NIGHTWALKER, COMMON c272 \u00a753",
            "lastName":"272\/53\/A"
            },
            {
            "firstName":"NIGHTWALKER, COMMON, 3RD OFFENSE c272 \u00a753",
            "lastName":"272\/53\/B"
            },
            {
            "firstName":"NOISY & DISORDERLY HOUSE, KEEP c272 \u00a753",
            "lastName":"272\/53\/I"
            },
            {
            "firstName":"NOTE, FORGERY OF COMMONWEALTH c. 267 s. 7",
            "lastName":"267.7"
            },
            {
            "firstName":"NOTE, UTTER WORTHLESS\/FALSE c. 267 s. 28",
            "lastName":"267.28"
            },
            {
            "firstName":"NOTES, POSSESS WORTHLESS\/FALSE c267 \u00a727",
            "lastName":"267\/27"
            },
            {
            "firstName":"NOXIOUS\/FILTHY SUBSTANCE, VANDALIZE WITH c266 \u00a7103",
            "lastName":"266\/103"
            },
            {
            "firstName":"NUISANCE, AID\/PERMIT c. 139 s. 20",
            "lastName":"139.2"
            },
            {
            "firstName":"NUISANCE, AID\/PERMIT c139 \u00a720",
            "lastName":"139\/20"
            },
            {
            "firstName":"NUMBER PLATE MISSING * c90 \u00a79",
            "lastName":"90\/9\/A"
            },
            {
            "firstName":"NUMBER PLATE VIOLATION * c90 \u00a76",
            "lastName":"90\/6"
            },
            {
            "firstName":"NUMBER PLATE VIOLATION TO CONCEAL ID c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"NUMBER PLATE VIOLATION TO CONCEAL ID c90 \u00a723",
            "lastName":"90\/23\/G"
            },
            {
            "firstName":"NUMBER PLATE, FAIL RETURN REPOSSESSED MV c90 \u00a76C",
            "lastName":"90\/6C"
            },
            {
            "firstName":"NUMBER PLATE, FALSE APPLIC FOR DEALER c. 90 s. 5(g)",
            "lastName":"90.5(g)"
            },
            {
            "firstName":"NUMBER PLATE, FALSE APPLIC FOR DEALER c90 \u00a75(g)",
            "lastName":"90\/5"
            },
            {
            "firstName":"NUMBER PLATE, MISUSE DEALER\/REPAIR 540 CMR \u00a718.04(2)",
            "lastName":"540CMR1804"
            },
            {
            "firstName":"NUMBER PLATE, MISUSE OFFICIAL * c90 \u00a72",
            "lastName":"90\/2\/C"
            },
            {
            "firstName":"NUMBER PLATE, TAKE OR ATTACH c266 \u00a7139(e)",
            "lastName":"266\/139\/E"
            },
            {
            "firstName":"OBSCENE MATTER TO MINOR c. 272 s. 28",
            "lastName":"272.28"
            },
            {
            "firstName":"OBSCENE MATTER TO MINOR c272 \u00a728",
            "lastName":"272\/28\/A"
            },
            {
            "firstName":"OBSCENE MATTER TO MINOR, 2ND AND SUBSQ. OFF. c. 272 s. 28",
            "lastName":"272.28"
            },
            {
            "firstName":"OBSCENE MATTER, DISTRIBUTE c. 272 s. 29",
            "lastName":"272.29"
            },
            {
            "firstName":"OBSCENE MATTER, DISTRIBUTE c272 \u00a729",
            "lastName":"272\/29\/A"
            },
            {
            "firstName":"OBSCENE MATTER, DISTRIBUTE, 3RD OFF. c272 \u00a729",
            "lastName":"272\/29\/C"
            },
            {
            "firstName":"OBSTRUCT JUSTICE (Common Law)",
            "lastName":"COMLAW7"
            },
            {
            "firstName":"OCCUPYING PUBLIC STREET W\/O PERMIT",
            "lastName":"51212|329-10"
            },
            {
            "firstName":"OFFICER ENGAGING SEX RELATIONS WITH INMATE OR PRISONER",
            "lastName":"268 . 21A"
            },
            {
            "firstName":"ONE-WAY STREET VIOLATION ( ONE WAY)",
            "lastName":"89\/10\/A"
            },
            {
            "firstName":"ONEWAY VIOLATION",
            "lastName":"89\/10"
            },
            {
            "firstName":"OPEN CONTAINER MARIJUANA IN VEHICLE c94G \u00a713(d)",
            "lastName":"94G\/13\/E"
            },
            {
            "firstName":"OPER AN UNREG. MV OR TRLR",
            "lastName":"90\/9"
            },
            {
            "firstName":"OPER MV AFT LIC. REVOKED",
            "lastName":"90\/23"
            },
            {
            "firstName":"OPER MV NEGLIG. TO ENDANGER",
            "lastName":"90\/24"
            },
            {
            "firstName":"OPER MV UN-INFL LIQ 4TH OR S",
            "lastName":"92\/24"
            },
            {
            "firstName":"OPER MV W\/O BEING LICENSED",
            "lastName":"90\/10"
            },
            {
            "firstName":"OPERATING AFTER REVOCATION OR SUSPENSION",
            "lastName":"31221|90-23"
            },
            {
            "firstName":"OPERATING M\/V WITHOUT A LICENSE",
            "lastName":"31214|90-10"
            },
            {
            "firstName":"OPERATING MOTOR VEHICLE TO ENDANGER c90 \u00a724",
            "lastName":"90\/24\/O1"
            },
            {
            "firstName":"OPERATING MV IN VIOLATON OF IGNITION INTERLOCK REST",
            "lastName":"90\/24\/S1"
            },
            {
            "firstName":"OPERATING UNREGISTERED MOTOR VEHICLE",
            "lastName":"c. 90 s. 9"
            },
            {
            "firstName":"OPERATION OF MOTOR VEHICLE, IMPROPER * c90 \u00a716",
            "lastName":"90\/16"
            },
            {
            "firstName":"OTHER OFFENSES",
            "lastName":"12600|"
            },
            {
            "firstName":"OTHER|AGGRESSIVE PANHANDLING",
            "lastName":"12411|"
            },
            {
            "firstName":"OTHER|ASSAULT",
            "lastName":"11111|"
            },
            {
            "firstName":"OTHER|ASSAULT DANG.WEAPON (209A)",
            "lastName":"12311|"
            },
            {
            "firstName":"OTHER|ASSAULT WITH INTENT TO RAPE",
            "lastName":"11511|"
            },
            {
            "firstName":"OTHER|ATT. KIDNAPPING",
            "lastName":"11211|"
            },
            {
            "firstName":"OTHER|ATTEMPTED ARSON",
            "lastName":"21611|"
            },
            {
            "firstName":"OTHER|ATTEMPTED UNARMED ROBBERY",
            "lastName":"11811|"
            },
            {
            "firstName":"OTHER|BEING PRESENT WHERE HEROIN\n                WAS KEPT",
            "lastName":"41411|"
            },
            {
            "firstName":"OTHER|BREAKING AND ENTERING BOAT DAYTIME",
            "lastName":"21111|"
            },
            {
            "firstName":"OTHER|BREAKING GLASS ON PUBLIC WAY",
            "lastName":"22211|"
            },
            {
            "firstName":"OTHER|CONSPIRACY TO VIOLATE DRUG LAWS",
            "lastName":"41311|"
            },
            {
            "firstName":"OTHER|DISTURBING SCHOOL ASSEMBLY",
            "lastName":"12611|"
            },
            {
            "firstName":"OTHER|DRINKING IN PUBLIC",
            "lastName":"41611|"
            },
            {
            "firstName":"OTHER|ELDER ABUSE; C19A S14",
            "lastName":"12511|"
            },
            {
            "firstName":"OTHER|ENTICING AWAY A PERSON FOR\n                PROSTITUTION\/ SEXUAL INTERCOURSE C272S2",
            "lastName":"11711|"
            },
            {
            "firstName":"OTHER|EXTORTIONS",
            "lastName":"21911|"
            },
            {
            "firstName":"OTHER|INTIMIDATION OF WITNESS",
            "lastName":"12111|"
            },
            {
            "firstName":"OTHER|LARCENY BY CHECK OVER $250 (266-37)",
            "lastName":"21411|"
            },
            {
            "firstName":"OTHER|LARCENY FROM A PERSON OVER $200",
            "lastName":"21211|"
            },
            {
            "firstName":"OTHER|LEFT TURN VIOLATION",
            "lastName":"31211|"
            },
            {
            "firstName":"OTHER|OP AFTER SUSPENSION, 2ND\n                SUBSEQUENT OFFENSE",
            "lastName":"31211|"
            },
            {
            "firstName":"OTHER|OPER. UNDER INFL. 3RD OFF",
            "lastName":"31111|"
            },
            {
            "firstName":"OTHER|PARENTAL KIDNAPPING",
            "lastName":"11211|"
            },
            {
            "firstName":"OTHER|POSS BURG TOOLS",
            "lastName":"21511|"
            },
            {
            "firstName":"OTHER|POSS CRACKPIPE",
            "lastName":"41511|"
            },
            {
            "firstName":"OTHER|POSS OF FRAUD ID 90:24B",
            "lastName":"21811|"
            },
            {
            "firstName":"OTHER|POSS OF LOADED FIREARM",
            "lastName":"12211|"
            },
            {
            "firstName":"OTHER|POSSES CL B DRUG SUBSQ OFF",
            "lastName":"41211|"
            },
            {
            "firstName":"OTHER|POSSESION OF 4 OR MORE STOLEN\n                CREDIT CARDS (266-37CC",
            "lastName":"21811|"
            },
            {
            "firstName":"OTHER|SEX FOR A FEE",
            "lastName":"11611|"
            },
            {
            "firstName":"OTHER|SHOPLIFTING BY CONCEALING\n                MDSE 266:30A",
            "lastName":"21311|"
            },
            {
            "firstName":"OTHER|STOLEN LICENSE PLATES,",
            "lastName":"22111|"
            },
            {
            "firstName":"OTHER|THREATS",
            "lastName":"11911|"
            },
            {
            "firstName":"OTHER|THREATS TO COMMIT A CRIME,\n                (BODILY HARM)",
            "lastName":"12411|"
            },
            {
            "firstName":"OTHER|UNAUTHORIZED REPRODUCTION OF\n                SOUND RECORDINGS (266-143A",
            "lastName":"21711|"
            },
            {
            "firstName":"OTHER|UNLAWFUL POSSESSION OF A\n                LOADED FIREARM (269-10N)",
            "lastName":"12211|"
            },
            {
            "firstName":"OTHER|UTTERING A FALSE PERSCRIPTION",
            "lastName":"41111|"
            },
            {
            "firstName":"OUI CHILD ENDANGERMENT, 1ST OFFENSE c90 \u00a724v",
            "lastName":"90\/24\/V1"
            },
            {
            "firstName":"OUI CHILD ENDANGERMENT, 2ND OFFENSE c90 \u00a724v",
            "lastName":"90\/24\/V2"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS & SERIOUS INJURY & NEGLIGENT c. 90 s. 24L(1)",
            "lastName":"90.24L(1)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS & SERIOUS INJURY & RECKLESS c. 90 s. 24L(1)",
            "lastName":"90.24L(1)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS & SERIOUS INJURY c. 90 s. 24L(2)",
            "lastName":"90.24L(2)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS c. 90 s. 24(1)(a)(1)",
            "lastName":"90.24(1)(a)(1)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS, 2ND OFF. c. 90 s. 24(1)(a)(1)",
            "lastName":"90.24(1)(a)(1)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS, 3RD OFF. c. 90 s. 24(1)(a)(1)",
            "lastName":"90.24(1)(a)(1)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS, 4TH OFF. c. 90 s. 24(1)(a)(1)",
            "lastName":"90.24(1)(a)(1)"
            },
            {
            "firstName":"OUI LIQUOR OR DRUGS, 5TH OFF. c. 90 s. 24(1)(a)(1)",
            "lastName":"90.24(1)(a)(1)"
            },
            {
            "firstName":"OUI\u00bfDRUGS & SERIOUS INJURY & NEGLIGENT c90 \u00a724L(1)",
            "lastName":"90\/24L\/B"
            },
            {
            "firstName":"OUI\u00bfDRUGS & SERIOUS INJURY & RECKLESS c90 \u00a724L(1)",
            "lastName":"90\/24L\/C"
            },
            {
            "firstName":"OUI\u00bfDRUGS & SERIOUS INJURY c90 \u00a724L(2)",
            "lastName":"90\/24L\/A"
            },
            {
            "firstName":"OUI\u00bfDRUGS c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/F"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 2ND OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/G"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 3RD OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/H"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 4TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/I"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 5TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/U"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 6TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/BB"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 7TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/CC"
            },
            {
            "firstName":"OUI\u00bfDRUGS, 9TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/EE"
            },
            {
            "firstName":"OUI\u00bfLIQUOR & SERIOUS INJURY & NEGLIGENT c90 \u00a724L(1)",
            "lastName":"90\/24L\/E"
            },
            {
            "firstName":"OUI\u00bfLIQUOR & SERIOUS INJURY & RECKLESS c90 \u00a724L(1)",
            "lastName":"90\/24L\/F"
            },
            {
            "firstName":"OUI\u00bfLIQUOR & SERIOUS INJURY c90 \u00a724L(2)",
            "lastName":"90\/24L\/D"
            },
            {
            "firstName":"OUI\u00bfLIQUOR c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/J"
            },
            {
            "firstName":"OUI\u00bfLIQUOR, 2ND OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/K"
            },
            {
            "firstName":"OUI\u00bfLIQUOR, 3RD OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/L"
            },
            {
            "firstName":"OUI\u00bfLIQUOR, 4TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/M"
            },
            {
            "firstName":"OUI\u00bfLIQUOR, 5TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/V"
            },
            {
            "firstName":"OUI\u00bfLIQUOR, 6TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/X"
            },
            {
            "firstName":"OUI\u00bfLIQUOR, 9TH OFFENSE c90 \u00a724(1)(a)(1)",
            "lastName":"90\/24\/AA"
            },
            {
            "firstName":"OUT-OF-SVCE ORDER VIOL, EMPLOYER PERMIT * c90F \u00a74(C)",
            "lastName":"90F\/4"
            },
            {
            "firstName":"OUT-OF-SVCE ORDER VIOLATION * c90F \u00a79(E\u00bd)(3)",
            "lastName":"90F\/9"
            },
            {
            "firstName":"OVERSIZE MV * c90 \u00a719",
            "lastName":"90\/19\/A"
            },
            {
            "firstName":"OXYCODENE, POSSESSION CLASS B WITH INTENT c94C \u00a732A(a)",
            "lastName":"94C\/32A\/Q"
            },
            {
            "firstName":"OXYCODONE, TRAFFICKING IN, OVER 100 GRAMS c94C \u00a732E(c)(3)",
            "lastName":"94C\/32E\/E"
            },
            {
            "firstName":"OXYCODONE, TRAFFICKING IN, OVER 14  GRAMS c94C \u00a732E(c)(1)",
            "lastName":"94C\/32E\/E1"
            },
            {
            "firstName":"OXYCODONE, TRAFFICKING IN, OVER 28  GRAMS c94C \u00a732E(c)(2)",
            "lastName":"94C\/32E\/E2"
            },
            {
            "firstName":"PARKING LOT, UNLICENSED c148 \u00a756",
            "lastName":"148\/56"
            },
            {
            "firstName":"PARKING TICKET, LESSEE FAIL PAY, 2ND OFF c90 \u00a720E(d)",
            "lastName":"90\/20E\/B"
            },
            {
            "firstName":"PARKING TICKET, MUTILATE c. 90 s. 20D",
            "lastName":"90.20D"
            },
            {
            "firstName":"PARKING TICKET, MUTILATE c90 \u00a720D",
            "lastName":"90\/20D"
            },
            {
            "firstName":"PASSING VIOLATION * c89 \u00a72",
            "lastName":"89\/2"
            },
            {
            "firstName":"PAWNBROKER, UNLICENSED c140 \u00a775",
            "lastName":"140\/75"
            },
            {
            "firstName":"PEDDLING BY MINOR, PERMIT UNLAWFUL c. 101 s. 20",
            "lastName":"101.2"
            },
            {
            "firstName":"PEDDLING BY MINOR, UNLAWFUL c101 \u00a719",
            "lastName":"101\/19"
            },
            {
            "firstName":"PEDDLING DOOR-TO-DOOR LICENSE, FALSE c. 101 s. 31",
            "lastName":"101.31"
            },
            {
            "firstName":"PEDDLING DOOR-TO-DOOR VIOLATION c. 101 s. 34",
            "lastName":"101.34"
            },
            {
            "firstName":"PEDDLING VIOLATION c101 \u00a714",
            "lastName":"101\/14\/A"
            },
            {
            "firstName":"PEDDLING WITHOUT A LICENSE c101 \u00a714",
            "lastName":"101\/14\/B"
            },
            {
            "firstName":"PEDESTRIAN VIOLATION c90 \u00a718A",
            "lastName":"90\/18A\/B"
            },
            {
            "firstName":"PERJURY c. 268 s. 1",
            "lastName":"268.1"
            },
            {
            "firstName":"PERJURY c268 \u00a71",
            "lastName":"268\/1\/A"
            },
            {
            "firstName":"PERJURY IN CAPITAL CASE c268 \u00a71",
            "lastName":"268\/1\/B"
            },
            {
            "firstName":"PERJURY IN TRIAL OF CAPITAL CASE c. 268 s. 1",
            "lastName":"268.1"
            },
            {
            "firstName":"PERJURY, ATTEMPT TO SUBORN c. 268 s. 3",
            "lastName":"268.3"
            },
            {
            "firstName":"PERJURY, ATTEMPT TO SUBORN c268 \u00a73",
            "lastName":"268\/3"
            },
            {
            "firstName":"PERJURY, SUBORN c. 268 s. 2",
            "lastName":"268.2"
            },
            {
            "firstName":"PERJURY, SUBORN c268 \u00a72",
            "lastName":"268\/2"
            },
            {
            "firstName":"PHENCYCLIDINE, DISTRIBUTE c94C \u00a732A(c)",
            "lastName":"94C\/32A\/M"
            },
            {
            "firstName":"PHENCYCLIDINE, DISTRIBUTE OR POSSESS WITH INTENT c. 94C s. 32A(c)",
            "lastName":"94C.32A(c)"
            },
            {
            "firstName":"PHENCYCLIDINE, DISTRIBUTE OR POSSESS WITH INTENT, SUBSQ. OFF. c. 94C s. 32A(d)",
            "lastName":"94C.32A(d)"
            },
            {
            "firstName":"PHENCYCLIDINE, POSSESS TO DISTRIB c94C \u00a732A(d)",
            "lastName":"94C\/32A\/O"
            },
            {
            "firstName":"PHENMETRAZINE, TRAFFICK IN c. 94C s. 32E(b)(2) - 28 to 100 g",
            "lastName":"94C.32E(b)(2)"
            },
            {
            "firstName":"PHENMETRAZINE, TRAFFICK IN c. 94C s. 32E(b)(3) - 100 to 200 g",
            "lastName":"94C.32E(b)(3)"
            },
            {
            "firstName":"PHENMETRAZINE, TRAFFICK IN c. 94C s. 32E(b)(4) - 200 g or more",
            "lastName":"94C.32E(b)(4)"
            },
            {
            "firstName":"PHENMETRAZINE, TRAFFICKING IN c. 94C s. 32E(b)(1) - 14 to 28 g",
            "lastName":"94C.32E(b)(1)"
            },
            {
            "firstName":"PHOTO, VIDEO, ELEC SURVEIL SECRETLY INITIMATE PART c272 \u00a7105",
            "lastName":"272\/105\/A"
            },
            {
            "firstName":"PHOTOGRAPH SEXUAL OR INITIMATE PART WO CONSENT c272 \u00a7105",
            "lastName":"272\/105\/C"
            },
            {
            "firstName":"PHOTOGRAPH, SECRETLY NUDE PERSON c272 \u00a7105",
            "lastName":"272\/105\/B"
            },
            {
            "firstName":"PHOTOGRAPH, UNSUSPECTING NUDE PERSON c272 \u00a7104\/B",
            "lastName":"272\/104\/B"
            },
            {
            "firstName":"PLATES, ATTACHING c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"PLAYGROUND EQUIPMENT, VANDALIZE c266 \u00a798A",
            "lastName":"266\/98A"
            },
            {
            "firstName":"POISONING  c. 265 s. 28",
            "lastName":"265.28"
            },
            {
            "firstName":"POISONING, ATTEMPTED c265 \u00a728",
            "lastName":"265\/28"
            },
            {
            "firstName":"POLICE HORSE\/DOG, MISTREAT\/INTERFERE c. 272 s. 77A",
            "lastName":"272.77A"
            },
            {
            "firstName":"POLICE HORSE\/DOG, MISTREAT\/INTERFERE c272 \u00a777A",
            "lastName":"272\/77A"
            },
            {
            "firstName":"POLICE OFFICER OR PUBLIC OFFICIAL, IMPERSONATE c. 268 s. 33",
            "lastName":"268.33"
            },
            {
            "firstName":"POLICE OFFICER, FAIL ASSIST c. 268 s. 24",
            "lastName":"268.24"
            },
            {
            "firstName":"POLICE OFFICER, FAIL ASSIST c268 \u00a724",
            "lastName":"268\/24"
            },
            {
            "firstName":"POLICE OFFICER, IMPERSONATE",
            "lastName":"268\/33"
            },
            {
            "firstName":"POLICE OFFICER, IMPERSONATE c268 \u00a733",
            "lastName":"268\/33\/A"
            },
            {
            "firstName":"POLICE OFFICER, INTERFERE WITH (Common Law)",
            "lastName":"COMLAW4"
            },
            {
            "firstName":"POLICE, MISLEADING c268 \u00a713",
            "lastName":"268\/13B"
            },
            {
            "firstName":"POLITICAL COMMITTEE & PERSONAL FUNDS,MIX c55 \u00a75",
            "lastName":"55\/5\/A"
            },
            {
            "firstName":"POLLUTANT CONTROL DEVICE, REMOVE c90 \u00a77O",
            "lastName":"90\/7O\/A"
            },
            {
            "firstName":"POLLUTE COASTAL WATERS c130 \u00a727",
            "lastName":"130\/27"
            },
            {
            "firstName":"POLYGAMY c. 272 s. 15",
            "lastName":"272.15"
            },
            {
            "firstName":"POLYGAMY c272 \u00a715",
            "lastName":"272\/15"
            },
            {
            "firstName":"POSS BURG. TOOLS",
            "lastName":"266\/49"
            },
            {
            "firstName":"POSS CLASS A W\/INT TO DISTRI",
            "lastName":"94C\/32"
            },
            {
            "firstName":"POSS CLASS B W\/ INT TO DISTR",
            "lastName":"94C\/32A"
            },
            {
            "firstName":"POSS CLASS C W\/ INT TO DISTR",
            "lastName":"94C\/32B"
            },
            {
            "firstName":"POSS CLASS D W\/INT TO DISTRI",
            "lastName":"94C\/32C"
            },
            {
            "firstName":"POSS CNTRFT SUB W\/INT DISTRI",
            "lastName":"94C\/32G"
            },
            {
            "firstName":"POSS FIREARM \/ AMMO W\/O FID",
            "lastName":"269\/10(H)"
            },
            {
            "firstName":"POSS HYPO SYRINGE, NEEDLE",
            "lastName":"94C\/27"
            },
            {
            "firstName":"POSS. DRUG PARAP W\/I TO SELL",
            "lastName":"94C\/32I"
            },
            {
            "firstName":"POSSESS TO DISTRIBUTE COCAINE, SUBSEQUENT. c94C \u00a732A(d)",
            "lastName":"94C\/32A\/D"
            },
            {
            "firstName":"POSSESSION OF A HYPODERMIC NEEDLE, DRUGS",
            "lastName":"41513|"
            },
            {
            "firstName":"POSSESSION OF A KNIFE, Malden Ordinance c.7 \u00a718",
            "lastName":"7MAL18"
            },
            {
            "firstName":"POSSESSION OF A SYRINGE, DRUGS",
            "lastName":"41514|"
            },
            {
            "firstName":"POSSESSION OF CLASS B, DRUGS",
            "lastName":"41313|94C-34"
            },
            {
            "firstName":"POSSESSION OF CLASS D, DRUGS",
            "lastName":"41315|94C-34"
            },
            {
            "firstName":"POSSESSION OF SAWED-OFF SHOTGUN OR\n                MACH. GUN",
            "lastName":"12213|269-10 (C)"
            },
            {
            "firstName":"POSSESSION OPEN CONTAINER ALCOHOL IN MV c. 90 s. 24I",
            "lastName":"90 . 24I"
            },
            {
            "firstName":"POSSESSION W\/I TO DISTRIBUTE, CLASS\n                B, DRUGS",
            "lastName":"41224|94C-32A"
            },
            {
            "firstName":"POULTRY, B&E OR ENTER TO STEAL c266 \u00a722",
            "lastName":"266\/22"
            },
            {
            "firstName":"PRESCRIPTION, UTTER FALSE c. 94C s. 33(b)",
            "lastName":"94C.33(b)"
            },
            {
            "firstName":"PRESCRIPTION, UTTER FALSE c94C \u00a733(b)",
            "lastName":"94C\/33\/E"
            },
            {
            "firstName":"PRESCRIPTION, UTTER FALSE, SUBSQ. OFF. c. 94C s. 33(b)",
            "lastName":"94C.33(b)"
            },
            {
            "firstName":"PRESCRIPTION, UTTER FALSE, SUBSQ.OFF. c94C \u00a733(c)",
            "lastName":"94C\/33\/F"
            },
            {
            "firstName":"PRESCRIPTION, WRITE IMPROPER c. 94C s. 22(a)",
            "lastName":"94C.22(a)"
            },
            {
            "firstName":"PRESCRIPTION, WRITE IMPROPER c94C \u00a722(a)",
            "lastName":"94C\/22\/C"
            },
            {
            "firstName":"PREVAIL WAGE, PRINTER FAIL PAY c5 \u00a71",
            "lastName":"5\/1\/A"
            },
            {
            "firstName":"PRISON GUARD HAVE SEX RELATIONS W\/PRISONER c268 \u00a721A",
            "lastName":"268\/21A"
            },
            {
            "firstName":"PRISONER DAMAGE JAIL\/HC PROPERTY c. 266 s. 130",
            "lastName":"266.13"
            },
            {
            "firstName":"PRISONER VANDALIZE JAIL\/HC PROPERTY c266 \u00a7130",
            "lastName":"266\/130"
            },
            {
            "firstName":"PRISONER VANDALIZE PRISON PROPERTY c266 \u00a7129",
            "lastName":"266\/129"
            },
            {
            "firstName":"PRISONER, DELIVER ARTICLE TO c268 \u00a728",
            "lastName":"268\/28\/B"
            },
            {
            "firstName":"PRISONER, DELIVER ARTICLE TO c268 \u00a731",
            "lastName":"268\/31\/A"
            },
            {
            "firstName":"PRISONER, DELIVER ARTICLE TO OR RECEIVE ARTICLE FROM c. 268 s. 31",
            "lastName":"268.31"
            },
            {
            "firstName":"PRISONER, DELIVER DRUGS OR ARTICLE TO c. 268 s. 28",
            "lastName":"268.28"
            },
            {
            "firstName":"PRISONER, DELIVER DRUGS TO c268 \u00a728",
            "lastName":"268\/28\/A"
            },
            {
            "firstName":"PROBATION \/ PAROLE VIOLATION",
            "lastName":"12623|"
            },
            {
            "firstName":"PROFESSIONAL LIC SUSPENDED,PRACTICE WITH c112 \u00a765",
            "lastName":"112\/65"
            },
            {
            "firstName":"PROMISSORY NOTE ENDORSEMENT, FORGERY OF c. 267 s. 1",
            "lastName":"267.1"
            },
            {
            "firstName":"PROPERTY DAMAGE TO INTIMIDATE c265 \u00a739(a)",
            "lastName":"265\/39\/C"
            },
            {
            "firstName":"PROSECUTOR, MISLEADING c268 \u00a713",
            "lastName":"268\/13B\/B1"
            },
            {
            "firstName":"PROSTITUTE, SOLICIT FOR c. 272 s. 8",
            "lastName":"272.8"
            },
            {
            "firstName":"PROSTITUTE, SOLICIT FOR c272 \u00a78",
            "lastName":"272\/8"
            },
            {
            "firstName":"PROSTITUTION NUISANCE, MAINTAIN  c139 \u00a74-\u00a75",
            "lastName":"139\/4"
            },
            {
            "firstName":"PROSTITUTION NUISANCE, MAINTAIN c. 139 s. 4 through 5",
            "lastName":"139.4 through 5"
            },
            {
            "firstName":"PROSTITUTION, DERIVE SUPPORT FROM c. 272 s. 7",
            "lastName":"272.7"
            },
            {
            "firstName":"PROSTITUTION, DERIVE SUPPORT FROM c272 \u00a77",
            "lastName":"272\/7"
            },
            {
            "firstName":"PROSTITUTION, DERIVE SUPPORT FROM CHILD c. 272 s. 4B",
            "lastName":"272.4B"
            },
            {
            "firstName":"PROSTITUTION, DERIVE SUPPORT FROM CHILD c272 \u00a74B",
            "lastName":"272\/4B"
            },
            {
            "firstName":"PROSTITUTION, INDUCE MINOR TO c. 272 s. 4A",
            "lastName":"272.4A"
            },
            {
            "firstName":"PROSTITUTION, INDUCE MINOR TO c272 \u00a74A",
            "lastName":"272\/4A"
            },
            {
            "firstName":"PROSTITUTION, KEEP HOUSE OF c. 272 s. 24",
            "lastName":"272.24"
            },
            {
            "firstName":"PROSTITUTION, KEEP HOUSE OF c272 \u00a724",
            "lastName":"272\/24"
            },
            {
            "firstName":"PROSTITUTION, MAINTAIN HOUSE OF c. 272 s. 6",
            "lastName":"272.6"
            },
            {
            "firstName":"PROSTITUTION, MAINTAIN HOUSE OF c272 \u00a76",
            "lastName":"272\/6"
            },
            {
            "firstName":"PROSTITUTION, PROCURE PERSON TO PRACTICE c. 272 s. 12",
            "lastName":"272.12"
            },
            {
            "firstName":"PROSTITUTION, PROCURE PERSON TO PRACTICE c272 \u00a712",
            "lastName":"272\/12\/A"
            },
            {
            "firstName":"PROSTITUTION\/UNLAW SEX,ABDUCT PERSON FOR  c272 \u00a72",
            "lastName":"272\/2"
            },
            {
            "firstName":"PROSTITUTION\/UNLAW SEX,ABDUCT PERSON FOR c. 272 s. 2",
            "lastName":"272.2"
            },
            {
            "firstName":"PROTECTIVE CUSTODY",
            "lastName":"PC"
            },
            {
            "firstName":"PUBLIC ACCOMMODATION, DISCRIMINATE IN c272 \u00a798",
            "lastName":"272\/98"
            },
            {
            "firstName":"PUBLIC ASSEMBLY, DISTURB c272 \u00a740",
            "lastName":"272\/40\/C"
            },
            {
            "firstName":"PUBLIC ASSEMBLY, DISTURB, 3RD\/SUBSQ.OFF. c272 \u00a740",
            "lastName":"272\/40\/D"
            },
            {
            "firstName":"PUBLIC ASSISTANCE FRAUD c. 18 s. 5B",
            "lastName":"18.5B"
            },
            {
            "firstName":"PUBLIC ASSISTANCE FRAUD c18 \u00a75B",
            "lastName":"18\/5B"
            },
            {
            "firstName":"PUBLIC EMPLOYEE ACCEPT\/SOLICIT BRIBE c268A \u00a72(b)",
            "lastName":"268A\/2\/A"
            },
            {
            "firstName":"PUBLIC EMPLOYEE ACCEPT\/SOLICIT GIFT c268A \u00a73(b)",
            "lastName":"268A\/3\/A"
            },
            {
            "firstName":"PUBLIC EMPLOYEE FIN STATEMENT, FALSE c268B \u00a77",
            "lastName":"268B\/7\/C"
            },
            {
            "firstName":"PUBLIC EMPLOYEE, BRIBE c268A \u00a72(a)",
            "lastName":"268A\/2\/B"
            },
            {
            "firstName":"PUBLIC EMPLOYEE, FALSE REPORT BY c. 268 s. 6A",
            "lastName":"268.6A"
            },
            {
            "firstName":"PUBLIC EMPLOYEE, FALSE REPORT BY c268 \u00a76A",
            "lastName":"268\/6A"
            },
            {
            "firstName":"PUBLIC EMPLOYEE, GIFT TO c268A \u00a73(a)",
            "lastName":"268A\/3\/B"
            },
            {
            "firstName":"PUBLIC EMPLOYEE\/WITNESS, BRIBE OR ACCEPT\/SOLICIT BRIBE c. 268A s. 2",
            "lastName":"268A.2"
            },
            {
            "firstName":"PUBLIC OFFICIAL, IMPERSONATE c268 \u00a733",
            "lastName":"268\/33\/B"
            },
            {
            "firstName":"PUBLIC WAY, THROW OBJECT ON c. 265 s. 35",
            "lastName":"265.35"
            },
            {
            "firstName":"PUBLIC WAY, THROW OBJECT ON c265 \u00a735",
            "lastName":"265\/35"
            },
            {
            "firstName":"PUPIL TRANSPORT VEHICLE VIOLATION * c90 \u00a77D",
            "lastName":"90\/7D\/A"
            },
            {
            "firstName":"PUPIL TRANSPORT VEHICLE, OVERCROWDED c. 90 s. 7D",
            "lastName":"90.7D"
            },
            {
            "firstName":"PUPIL TRANSPORT VEHICLE, OVERCROWDED c90 \u00a77D",
            "lastName":"90\/7D\/B"
            },
            {
            "firstName":"PUPILS, TRANSPORT WITHOUT LICENSE * c90 \u00a78A\u00bd",
            "lastName":"90\/8A12"
            },
            {
            "firstName":"PURCHASING VIOLATION, GOVERNMENT c266 \u00a767A",
            "lastName":"266\/67A"
            },
            {
            "firstName":"RACING MOTOR VEHICLE * c90 \u00a717B",
            "lastName":"90\/17B\/A"
            },
            {
            "firstName":"RACING MOTOR VEHICLE c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"RACING MOTOR VEHICLE c90 \u00a724(2)(a)",
            "lastName":"90\/24\/N"
            },
            {
            "firstName":"RACING MOTOR VEHICLE, SUBSQ.OFF. * c90 \u00a717B",
            "lastName":"90\/17B\/B"
            },
            {
            "firstName":"RACING PARIMUTUEL TICKET, FALSE c128A \u00a710B",
            "lastName":"128A\/10B"
            },
            {
            "firstName":"RAFFLE\/BAZAAR VIOLATION c271 \u00a77A",
            "lastName":"271\/7A"
            },
            {
            "firstName":"RAILROAD CAR, B&E FOR FELONY c266 \u00a719",
            "lastName":"266\/19\/A"
            },
            {
            "firstName":"RAILROAD CAR, B&E OR ENTER AT NIGHT, FOR FELONY c. 266 s. 19",
            "lastName":"266.19"
            },
            {
            "firstName":"RAILROAD CAR, ENTER AT NIGHT FOR FELONY c266 \u00a719",
            "lastName":"266\/19\/B"
            },
            {
            "firstName":"RAILROAD CAR, LARCENY FROM c266 \u00a720",
            "lastName":"266\/20\/C"
            },
            {
            "firstName":"RAILROAD CAR, THROW MISSILE AT c159 \u00a7104",
            "lastName":"159\/104\/C"
            },
            {
            "firstName":"RAILROAD CAR\/TRACK\/SIGNAL, VANDALIZE c159 \u00a7103",
            "lastName":"159\/103\/A"
            },
            {
            "firstName":"RAILROAD CONDUCTOR, ASSAULT c159 \u00a7104",
            "lastName":"159\/104\/D"
            },
            {
            "firstName":"RAILROAD CROSSING VIOLATION * c90 \u00a715",
            "lastName":"90\/15\/A"
            },
            {
            "firstName":"RAILROAD FARE, ATTEMPT TO EVADE c159 \u00a7101",
            "lastName":"159\/101\/C"
            },
            {
            "firstName":"RAILROAD FARE, EVADE c. 160 s. 220",
            "lastName":"160.22"
            },
            {
            "firstName":"RAILROAD FARE, EVADE c159 \u00a7101",
            "lastName":"159\/101\/D"
            },
            {
            "firstName":"RAILROAD FARE, EVADE c160 \u00a7220",
            "lastName":"160\/220"
            },
            {
            "firstName":"RAILROAD STATION, LOITER IN c160 \u00a7219",
            "lastName":"160\/219"
            },
            {
            "firstName":"RAILROAD TICKET, FORGE c267 \u00a72",
            "lastName":"267\/2\/A"
            },
            {
            "firstName":"RAILROAD TICKET, IMPROP SELL DISCOUNT c. 160 s. 198A",
            "lastName":"160.198A"
            },
            {
            "firstName":"RAILROAD TICKET, UTTER FALSE c267 \u00a76",
            "lastName":"267\/6\/A"
            },
            {
            "firstName":"RAILROAD TRACK, WALK\/RIDE ON c160 \u00a7218",
            "lastName":"160\/218"
            },
            {
            "firstName":"RAILROAD TRACK, WALK\/STAND ON ELECTRIC c162 \u00a718",
            "lastName":"162\/18"
            },
            {
            "firstName":"RAILROAD, GROSS NEGLIGENCE IN MANAGING c160 \u00a7231",
            "lastName":"160\/231"
            },
            {
            "firstName":"RAILROAD, MALICIOUSLY STOP c160 \u00a7227",
            "lastName":"160\/227"
            },
            {
            "firstName":"RAILROAD, OBSTRUCT\/ENDANGER c. 160 s. 226",
            "lastName":"160.226"
            },
            {
            "firstName":"RAILROAD, OBSTRUCT\/ENDANGER c160 \u00a7226",
            "lastName":"160\/226"
            },
            {
            "firstName":"RAILROAD\/CARRIER RECORDKEEPING VIOL c159 \u00a731",
            "lastName":"159\/31"
            },
            {
            "firstName":"RAILROAD\/RAILWAY STATION, LITTER IN c161 \u00a794A",
            "lastName":"161\/94A"
            },
            {
            "firstName":"RAILROAD\/RAILWAY STATION, LOITER IN c161 \u00a795",
            "lastName":"161\/95"
            },
            {
            "firstName":"RAPE",
            "lastName":"265\/22\/A"
            },
            {
            "firstName":"RAPE AND ABUSE OF A CHILD UNDER 16",
            "lastName":"11522|265:23"
            },
            {
            "firstName":"RAPE c. 265 s. 22(b)",
            "lastName":"265.22(b)"
            },
            {
            "firstName":"RAPE c265 \u00a722(b)",
            "lastName":"265\/22"
            },
            {
            "firstName":"RAPE OF CHILD WITH FORCE c. 265 s. 22A",
            "lastName":"265.22A"
            },
            {
            "firstName":"RAPE OF CHILD WITH FORCE c265 \u00a722A",
            "lastName":"265\/22A\/A"
            },
            {
            "firstName":"RAPE OF CHILD WITH FORCE, AGGRAVATED c265 \u00a722A",
            "lastName":"265\/22B"
            },
            {
            "firstName":"RAPE OF CHILD WITH FORCE, ARMED, FIREARM c. 265 s. 22A",
            "lastName":"265.22A"
            },
            {
            "firstName":"RAPE OF CHILD WITH FORCE, SUBSQ. OFF. c. 265 s. 22A",
            "lastName":"265.22A"
            },
            {
            "firstName":"RAPE OF CHILD WITH FORCE, SUBSQ.OFF. c265 \u00a722A",
            "lastName":"265\/22A\/B"
            },
            {
            "firstName":"RAPE OF CHILD, AGGRAVATED, FIVE YEAR AGE DIFF c265 \u00a723A",
            "lastName":"265\/23A\/A"
            },
            {
            "firstName":"RAPE OF CHILD, AGGRAVATED, TEN YEAR AGE DIFF c265 \u00a723",
            "lastName":"265\/23A\/B"
            },
            {
            "firstName":"RAPE OF CHILD, STATUTORY AGGRAVATED c265 \u00a723A\/A",
            "lastName":"265\/23\/A\/A"
            },
            {
            "firstName":"RAPE OF CHILD, STATUTORY c. 265 s. 23",
            "lastName":"265.23"
            },
            {
            "firstName":"RAPE OF CHILD, STATUTORY c265 \u00a723",
            "lastName":"265\/23\/A"
            },
            {
            "firstName":"RAPE OF CHILD, STATUTORY, SUBSQ. OFF. c. 265 s. 23",
            "lastName":"265.23"
            },
            {
            "firstName":"RAPE OF CHILD, STATUTORY, SUBSQ.OFF. c265 \u00a723",
            "lastName":"265\/23\/B"
            },
            {
            "firstName":"RAPE, AGGRAVATED c. 265 s. 22(a)",
            "lastName":"265.22(a)"
            },
            {
            "firstName":"RAPE, AGGRAVATED c265 \u00a722(a)",
            "lastName":"265\/22\/B"
            },
            {
            "firstName":"RAPE, AGGRAVATED FIREARM-ARMED c265 \u00a722(a)",
            "lastName":"265\/22\/F"
            },
            {
            "firstName":"RAPE, AGGRAVATED FIREARM-ARMED, SUBSQ.OFF. c265 \u00a722(a)",
            "lastName":"265\/22\/G"
            },
            {
            "firstName":"RAPE, AGGRAVATED, ARMED, FIREARM c. 265 s. 22(a)",
            "lastName":"265.22(a)"
            },
            {
            "firstName":"RAPE, AGGRAVATED, SUBSQ. OFF. c. 265 s. 22(a)",
            "lastName":"265.22(a)"
            },
            {
            "firstName":"RAPE, AGGRAVATED, SUBSQ.OFF. c265 \u00a722(a)",
            "lastName":"265\/22\/C"
            },
            {
            "firstName":"RAPE, ARMED, FIREARM c. 265 s. 22(b)",
            "lastName":"265.22(b)"
            },
            {
            "firstName":"RAPE, FIREARM-ARMED c265 \u00a722(b)",
            "lastName":"265\/22\/E"
            },
            {
            "firstName":"RAPE, SUBSQ. OFF. c. 265 s. 22(b)",
            "lastName":"265.22(b)"
            },
            {
            "firstName":"RAPE, SUBSQ.OFF. c265 \u00a722(b)",
            "lastName":"265\/22\/D"
            },
            {
            "firstName":"REC&APOS;G STOLEN PROP $250 MORE",
            "lastName":"266\/60"
            },
            {
            "firstName":"RECEIVE FALSE-TRADED PROPERTY +$250 c266 \u00a760",
            "lastName":"266\/60\/D"
            },
            {
            "firstName":"RECEIVE STOLEN OR FALSE-TRADED PROPERTY -$250 c. 266 s. 60",
            "lastName":"266.6"
            },
            {
            "firstName":"RECEIVE STOLEN OR FALSE-TRADED PROPERTY +$250 c. 266 s. 60 ",
            "lastName":"266.6"
            },
            {
            "firstName":"RECEIVE STOLEN OR FALSELY TRADED PROPERTY -$250 SUBSQ. OFF. c. 266 s. 60",
            "lastName":"266.6"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY -$1200 c266 \u00a760",
            "lastName":"266\/60\/B1"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY -$1200, SUBSQ. OFF c266 \u00a760",
            "lastName":"266\/60\/C1"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY -$250 c266 \u00a760",
            "lastName":"266\/60\/B"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY -$250, SUBSQ.OFF c266 \u00a760",
            "lastName":"266\/60\/C"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY +$1200 c266 \u00a760",
            "lastName":"266\/60\/A1"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY +$250 c266 \u00a760",
            "lastName":"266\/60\/A"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY +1200, SUBSQ.OFF c266 \u00a760",
            "lastName":"266\/60\/J1"
            },
            {
            "firstName":"RECEIVE STOLEN PROPERTY +250, SUBSQ.OFF c266 \u00a760",
            "lastName":"266\/60\/J"
            },
            {
            "firstName":"RECEIVER, COMMON c. 266 s. 62",
            "lastName":"266.62"
            },
            {
            "firstName":"RECEIVER, COMMON c266 \u00a762",
            "lastName":"266\/62"
            },
            {
            "firstName":"RECEIVING STOLEN MOTOR VEHICLE",
            "lastName":"21515|266-28"
            },
            {
            "firstName":"RECKLESS ENDANGERMENT OF CHILD  c265 \u00a713L",
            "lastName":"265\/13L"
            },
            {
            "firstName":"RECKLESS OPERATION OF MOTOR VEHICLE c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"RECKLESS OPERATION OF MOTOR VEHICLE c90 \u00a724(2)(a)",
            "lastName":"90\/24\/O"
            },
            {
            "firstName":"RECOGNIZANCE OR BAIL, FAIL APPEAR ON MISDEMEANOR c. 276 s. 82A",
            "lastName":"276.82A"
            },
            {
            "firstName":"RECOGNIZANCE OR BAIL; FAIL TO APPEAR ON FELONY c. 276 s. 82A",
            "lastName":"276.82A"
            },
            {
            "firstName":"RECOGNIZANCE, FAIL APPEAR UPON c276 \u00a782A",
            "lastName":"276\/82A"
            },
            {
            "firstName":"RECORDING OF LIVE PERFORMANCE, UNAUTH c. 266 s. 143B - Small Quantity",
            "lastName":"266.143B"
            },
            {
            "firstName":"RECORDING OF LIVE PERFORMANCE, UNAUTH c266 \u00a7143B",
            "lastName":"266\/143B"
            },
            {
            "firstName":"RECORDING W\/OUT MFR NAME, MFR\/SELL\/RENT c. 266 s. 143C - Large Quantity",
            "lastName":"266.143C"
            },
            {
            "firstName":"RECORDING W\/OUT MFR NAME, MFR\/SELL\/RENT c266 \u00a7143C",
            "lastName":"266\/143C"
            },
            {
            "firstName":"RECORDING, UNAUTHORIZED REPRODUCTION OF c. 266 s. 143A - Large Quantity",
            "lastName":"266.143A"
            },
            {
            "firstName":"RECORDING, UNAUTHORIZED REPRODUCTION OF c. 266 s. 143A - Medium Quantity",
            "lastName":"266.143A"
            },
            {
            "firstName":"RECORDING, UNAUTHORIZED REPRODUCTION OF c. 266 s. 143A - Small Quantity",
            "lastName":"266.143A"
            },
            {
            "firstName":"RECORDING, UNAUTHORIZED REPRODUCTION OF c266 \u00a7143A",
            "lastName":"266\/143A"
            },
            {
            "firstName":"RED LIGHT VIOLATION",
            "lastName":"89\/9\/A"
            },
            {
            "firstName":"RED\/BLUE LIGHT VIOLATION, MV * c90 \u00a77E",
            "lastName":"90\/7E"
            },
            {
            "firstName":"REGISTER MV OPERATED +30 DAYS YEAR, FL * c90 \u00a73",
            "lastName":"90\/3\/A"
            },
            {
            "firstName":"REGISTERED LAND, CONVEY ENCUMBERED c. 185 s. 118",
            "lastName":"185.118"
            },
            {
            "firstName":"REGISTRATION LEFT IN TRANSFERRED MV * c90 \u00a72B",
            "lastName":"90\/2B"
            },
            {
            "firstName":"REGISTRATION NOT IN POSSESSION * c90 \u00a711",
            "lastName":"90\/11\/B"
            },
            {
            "firstName":"REGISTRATION STICKER MISSING * 540 CMR \u00a72.05(6)(a)",
            "lastName":"540CMR205"
            },
            {
            "firstName":"REGISTRATION STICKER MISSING * 540 CMR \u00a72.24(3)",
            "lastName":"540CMR224"
            },
            {
            "firstName":"REGISTRATION SUSPENDED, OP MV WITH c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"REGISTRATION SUSPENDED, OP MV WITH c90 \u00a723",
            "lastName":"90\/23\/H"
            },
            {
            "firstName":"REGISTRATION SUSPENDED, OP MV, SUBSQ.OFF c. 90 s. 23",
            "lastName":"90.23"
            },
            {
            "firstName":"REGISTRATION SUSPENDED, OP MV, SUBSQ.OFF c90 \u00a723",
            "lastName":"90\/23\/I"
            },
            {
            "firstName":"REGISTRATION, FALSE STATEMNT IN APPL FOR c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"REGISTRATION, FALSE STATEMNT IN APPL FOR c90 \u00a724(2)(a)",
            "lastName":"90\/24\/T"
            },
            {
            "firstName":"REGISTRATION, FL SURRENDER ON TRANSFER * c90 \u00a72",
            "lastName":"90\/2\/A"
            },
            {
            "firstName":"RELIGIOUS SERVICE, DISTURB c. 272 s. 38",
            "lastName":"272.38"
            },
            {
            "firstName":"RELIGIOUS SERVICE, DISTURB c272 \u00a738",
            "lastName":"272\/38"
            },
            {
            "firstName":"RESIST ARREST (Common Law)",
            "lastName":"COMLAW5"
            },
            {
            "firstName":"RESIST ARREST c268 \u00a732B",
            "lastName":"268\/32B"
            },
            {
            "firstName":"RESIST, ARREST c. 268 s. 32B",
            "lastName":"268.32B"
            },
            {
            "firstName":"RESTAURANT, DEFRAUD c. 140 s. 12",
            "lastName":"140.12"
            },
            {
            "firstName":"RESTAURANT, DEFRAUD c140 \u00a712",
            "lastName":"140\/12\/A"
            },
            {
            "firstName":"RETURN BY PROCESS SERVER, FALSE  c268 \u00a76B",
            "lastName":"268\/6B"
            },
            {
            "firstName":"RIDE IN BACK OF TRAILER\/SEMI c90 \u00a713",
            "lastName":"90\/13\/E"
            },
            {
            "firstName":"RIDE IN BACK OF TRAILER\/SEMI, 3RD OFF. c90 \u00a713",
            "lastName":"90\/13\/G"
            },
            {
            "firstName":"RIFLE\/SHOTGUN IN VEH, LEAVE LARGE CAPACITY c140 \u00a7131C(c)",
            "lastName":"140\/131C\/B"
            },
            {
            "firstName":"RIFLE\/SHOTGUN ON WAY, CARRY LOADED c. 269 s. 12D(a)",
            "lastName":"269.12D(a)"
            },
            {
            "firstName":"RIFLE\/SHOTGUN ON WAY, CARRY LOADED c269 \u00a712D",
            "lastName":"269\/12D"
            },
            {
            "firstName":"RIFLE\/SHOTGUN ON WAY, CARRY LOADED c269 \u00a712D(a)",
            "lastName":"269\/12D\/A"
            },
            {
            "firstName":"RIFLE\/SHOTGUN ON WAY, CARRY UNLOADED c269 \u00a712D(b)",
            "lastName":"269\/12D\/B"
            },
            {
            "firstName":"RIFLE\/SHOTGUN W\/O SERIAL NO., SELL c. 269 s. 10(g)",
            "lastName":"269.10(g)"
            },
            {
            "firstName":"RIFLE\/SHOTGUN WITHOUT SERIAL NO., SELL c269 \u00a710(g)",
            "lastName":"269\/10\/R"
            },
            {
            "firstName":"RIFLE\/SHOTGUN, STORE IMPROP NEAR MINOR c140 \u00a7131L(a)&(c)",
            "lastName":"140\/131L\/D"
            },
            {
            "firstName":"RIFLE\/SHOTGUN, STORE IMPROPER NEAR MINOR c. 140 s. 131L(a)",
            "lastName":"140.131L(a) "
            },
            {
            "firstName":"RIGHT LANE, FAIL DRIVE IN * c89 \u00a74B",
            "lastName":"89\/4B\/B"
            },
            {
            "firstName":"RIOT",
            "lastName":"12419|269-01"
            },
            {
            "firstName":"RIOT, FAIL DISPERSE c269 \u00a72",
            "lastName":"269\/2\/A"
            },
            {
            "firstName":"RIOT, FAIL DISPERSE OR FAIL ASSIST IN DISPERSING c. 269 s. 2",
            "lastName":"269.2"
            },
            {
            "firstName":"RIOT, INCITE c264 \u00a711",
            "lastName":"264\/11"
            },
            {
            "firstName":"RIOT, OFFICIAL FAIL DISPERSE c269 \u00a73",
            "lastName":"269\/3"
            },
            {
            "firstName":"RMV DOCUMENT OR SIGNATURE, POSSESS FALSE\/STOLEN, MISUSE\/FORGE c. 90 s. 24B",
            "lastName":"90.24B"
            },
            {
            "firstName":"RMV DOCUMENT, FORGE\/MISUSE c90 \u00a724B",
            "lastName":"90\/24B\/B"
            },
            {
            "firstName":"RMV DOCUMENT, POSSESS\/USE FALSE\/STOLEN c90 \u00a724B",
            "lastName":"90\/24B\/C"
            },
            {
            "firstName":"RMV ID CARD ADDRESS CHANGE c90 \u00a78J",
            "lastName":"90\/8J\/A"
            },
            {
            "firstName":"RMV ID CARD FRAUD c90 \u00a78H",
            "lastName":"90\/8H\/A"
            },
            {
            "firstName":"RMV ID CARD REPLACEMENT VIOL c90 \u00a78G",
            "lastName":"90\/8G\/A"
            },
            {
            "firstName":"RMV SIGNATURE, FORGE\/MISUSE c90 \u00a724B",
            "lastName":"90\/24B\/D"
            },
            {
            "firstName":"RMV SIGNATURE, POSSESS\/USE FALSE\/STOLEN c90 \u00a724B",
            "lastName":"90\/24B\/E"
            },
            {
            "firstName":"ROBBERY +60, UNARMED c. 265 s. 19(a)",
            "lastName":"265.19(a)"
            },
            {
            "firstName":"ROBBERY +60, UNARMED c265 \u00a719(a)",
            "lastName":"265\/19\/A"
            },
            {
            "firstName":"ROBBERY +60, UNARMED, SUBSQ. OFF. c. 265 s. 19(a)",
            "lastName":"265.19(a)"
            },
            {
            "firstName":"ROBBERY +60, UNARMED, SUBSQ.OFF. c265 \u00a719(a)",
            "lastName":"265\/19\/B"
            },
            {
            "firstName":"ROBBERY, ARMED & MASKED c. 265 s. 17 ",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, ARMED & MASKED c265 \u00a717",
            "lastName":"265\/17\/B"
            },
            {
            "firstName":"ROBBERY, ARMED & MASKED, SUBSQ. OFF. c. 265 s. 17",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, ARMED & MASKED, SUBSQ.OFF. c265 \u00a717",
            "lastName":"265\/17\/C"
            },
            {
            "firstName":"ROBBERY, ARMED c. 265 s. 17 ",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, ARMED c265 \u00a717",
            "lastName":"265\/17\/A"
            },
            {
            "firstName":"ROBBERY, ARMED, FIREARM & MASKED c. 265 s. 17 ",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, ARMED, FIREARM & MASKED, SUBSQ.  c. 265 s. 17 ",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, ARMED, FIREARM c. 265 s. 17 ",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, ARMED, FIREARM, SUBSQ. c. 265 s. 17 ",
            "lastName":"265.17"
            },
            {
            "firstName":"ROBBERY, FIREARM-ARMED & MASKED c265 \u00a717",
            "lastName":"265\/17\/F"
            },
            {
            "firstName":"ROBBERY, FIREARM-ARMED & MASKED, SUBSQ.OFF. c265 \u00a717",
            "lastName":"265\/17\/G"
            },
            {
            "firstName":"ROBBERY, FIREARM-ARMED c265 \u00a717",
            "lastName":"265\/17\/D"
            },
            {
            "firstName":"ROBBERY, FIREARM-ARMED, SUBSQ.OFF. c265 \u00a717",
            "lastName":"265\/17\/E"
            },
            {
            "firstName":"ROBBERY, UNARMED c. 265 s. 19(b)",
            "lastName":"265.19(b)"
            },
            {
            "firstName":"ROBBERY, UNARMED c265 \u00a719(b)",
            "lastName":"265\/19\/C"
            },
            {
            "firstName":"SAFEKEEPING ARREST",
            "lastName":"61413|"
            },
            {
            "firstName":"SAFETY GLASS VIOLATION * c90 \u00a79A",
            "lastName":"90\/9A"
            },
            {
            "firstName":"SAFETY STANDARDS, MV NOT MEETING RMV * c90 \u00a77A & \u00a720",
            "lastName":"90\/20\/A"
            },
            {
            "firstName":"SALES TAX CERTIFICATE, FALSE c62C \u00a773(i)",
            "lastName":"62C\/73\/A"
            },
            {
            "firstName":"SAMARITAN VEHICLE MISUSE SIREN\/LIGHT * c90 \u00a77I",
            "lastName":"90\/7I"
            },
            {
            "firstName":"SCALLOPS SALES VIOLATION c130 \u00a792",
            "lastName":"130\/92\/B"
            },
            {
            "firstName":"SCHOOL BUS INSPECTION, FAIL PERFORM POST-TRIP * c90 \u00a77B(17)",
            "lastName":"90\/7B\/F"
            },
            {
            "firstName":"SCHOOL BUS OPERATION\/EQUIPMENT VIOL * c90 \u00a77B",
            "lastName":"90\/7B\/A"
            },
            {
            "firstName":"SCHOOL BUS, FAIL STOP FOR * c90 \u00a714",
            "lastName":"90\/14\/C"
            },
            {
            "firstName":"SCHOOL BUS, OVERCROWDED c. 90 s. 7B",
            "lastName":"90.7B"
            },
            {
            "firstName":"SCHOOL BUS, OVERCROWDED c90 \u00a77B",
            "lastName":"90\/7B\/B"
            },
            {
            "firstName":"SCHOOL OR PUBLIC ASSEMBLY, DISTURB c. 272 s. 40",
            "lastName":"272.4"
            },
            {
            "firstName":"SCHOOL OR PUBLIC ASSEMBLY, DISTURB, 3RD AND SUBSQ. OFF. c. 272 s. 40",
            "lastName":"272.4"
            },
            {
            "firstName":"SCHOOL, DISTURB c272 \u00a740",
            "lastName":"272\/40\/A"
            },
            {
            "firstName":"SCHOOL, DISTURB, 3RD OFF. c272 \u00a740",
            "lastName":"272\/40\/B"
            },
            {
            "firstName":"SCHOOL, FAIL SEND CHILD TO c76 \u00a72",
            "lastName":"76\/2"
            },
            {
            "firstName":"SCHOOL, POSSESS LIQUOR IN c. 272 s. 40A",
            "lastName":"272.40A"
            },
            {
            "firstName":"SCHOOL, VANDALIZE c266 \u00a798",
            "lastName":"266\/98\/A"
            },
            {
            "firstName":"SEAT BELT, FAIL WEAR * c90 \u00a713A",
            "lastName":"90\/13A"
            },
            {
            "firstName":"SECOND OR SUBSEQUENT, POSSESS LARGE CAPACITY FIREARM c269 \u00a710(m)",
            "lastName":"269\/10\/B"
            },
            {
            "firstName":"SELF DEFENSE SPRAY,  POSS BY FELON\/YO c. 140 \u00a7122D\/A",
            "lastName":"140\/122D\/A"
            },
            {
            "firstName":"SELF-INSURER FAIL NOTIFY OF SUIT c. 90 s. 34F",
            "lastName":"90.34F"
            },
            {
            "firstName":"SERVICE FOR OTHER DEPARTMENT",
            "lastName":"12622|"
            },
            {
            "firstName":"SEWER BY-LAW VIOLATION c40 \u00a721(6)",
            "lastName":"40\/21\/D"
            },
            {
            "firstName":"SEX OFFENDER FAIL TO REGISTER c6 \u00a7178H(a)-(c)",
            "lastName":"6\/178H\/A"
            },
            {
            "firstName":"SEX OFFENDER FAIL TO REGISTER, HOMELESS, 2ND OFF. c6 \u00a7178H(c)",
            "lastName":"6\/178H\/C"
            },
            {
            "firstName":"SEX OFFENDER FAIL TO REGISTER, HOMELESS, 3RD OFF. c6 \u00a7178H(c)",
            "lastName":"6\/178H\/D"
            },
            {
            "firstName":"SEX OFFENDER FAIL TO REGISTER, LEVEL 2 or 3 c6 \u00a7178H(a)(1)",
            "lastName":"6\/178H\/E"
            },
            {
            "firstName":"SEX OFFENDER FAIL TO REGISTER, SUBSQ.OFF. c6 \u00a7178H(a)",
            "lastName":"6\/178H\/B"
            },
            {
            "firstName":"SEX OFFENDER FAIL TO REGISTER, SUBSQ.OFF. LEVEL 2 OR 3 c6 \u00a7178H(a)",
            "lastName":"6\/178H\/G"
            },
            {
            "firstName":"SEX OFFENDER INFO, AGENCY FAIL PROVIDE c6 \u00a7178K(3)",
            "lastName":"6\/178K"
            },
            {
            "firstName":"SEX OFFENDER INFO, HOMELESS SHELTER FAIL PROVIDE c6 \u00a7178F or \u00a7178F\u00bd",
            "lastName":"6\/178F"
            },
            {
            "firstName":"SEX OFFENDER REGISTRY INFORMATION, ILLEGAL USE OF c. 6 s. 178N",
            "lastName":"6.178N"
            },
            {
            "firstName":"SEXUAL CONDUCT FOR FEE c272 \u00a753A",
            "lastName":"272\/53A\/A"
            },
            {
            "firstName":"SEXUAL CONDUCT, PAY FOR c272 \u00a753A",
            "lastName":"272\/53A\/B"
            },
            {
            "firstName":"SEXUAL CONDUCT, PAY FOR OR FOR FEE c. 272 s. 53A",
            "lastName":"272.53A"
            },
            {
            "firstName":"SEXUAL INTERCOURSE, DRUG FOR c. 272 s. 3",
            "lastName":"272.3"
            },
            {
            "firstName":"SEXUAL INTERCOURSE, DRUG FOR c272 \u00a73",
            "lastName":"272\/3"
            },
            {
            "firstName":"SEXUAL INTERCOURSE, INDUCE CHASTE MINOR c. 272 s. 4",
            "lastName":"272.4"
            },
            {
            "firstName":"SEXUAL INTERCOURSE, INDUCE CHASTE MINOR c272 \u00a74",
            "lastName":"272\/4"
            },
            {
            "firstName":"SEXUALLY DANGEROUS PERSON c123A",
            "lastName":"123A"
            },
            {
            "firstName":"SHELLFISH IN CONTAMINATED AREA AT NIGHT c130 \u00a775",
            "lastName":"130\/75\/C"
            },
            {
            "firstName":"SHELLFISH IN CONTAMINATED AREA c. 130 s. 75",
            "lastName":"130.75"
            },
            {
            "firstName":"SHELLFISH IN CONTAMINATED AREA c130 \u00a775",
            "lastName":"130\/75\/B"
            },
            {
            "firstName":"SHELLFISH SALES VIOLATION c. 130 s. 81",
            "lastName":"130.81"
            },
            {
            "firstName":"SHOPLIFTING $100+ BY ASPORTATION c266 \u00a730A",
            "lastName":"266\/30A\/S"
            },
            {
            "firstName":"SHOPLIFTING $100+ BY CONCEALING MDSE c266 \u00a730A",
            "lastName":"266\/30A\/T"
            },
            {
            "firstName":"SHOPLIFTING $100+ BY PRICE TAG TAMPERING c266 \u00a730A",
            "lastName":"266\/30A\/U"
            },
            {
            "firstName":"SHOPLIFTING $100+ BY RECORDING FALSE VALUE c266 \u00a730A",
            "lastName":"266\/30A\/W"
            },
            {
            "firstName":"SHOPLIFTING $100+ OF SHOPPING CART c266 \u00a730A",
            "lastName":"266\/30A\/X"
            },
            {
            "firstName":"SHOPLIFTING $250+ BY ASPORTATION c266 \u00a730A",
            "lastName":"266\/30A\/S"
            },
            {
            "firstName":"SHOPLIFTING $250+ BY CONCEALING MDSE c266 \u00a730A",
            "lastName":"266\/30A\/T"
            },
            {
            "firstName":"SHOPLIFTING $250+ BY PRICE TAG TAMPERING c266 \u00a730A",
            "lastName":"266\/30A\/U"
            },
            {
            "firstName":"SHOPLIFTING $250+ BY RECORDING FALSE VALUE c266 \u00a730A",
            "lastName":"266\/30A\/W"
            },
            {
            "firstName":"SHOPLIFTING $250+ OF SHOPPING CART c266 \u00a730A",
            "lastName":"266\/30A\/X"
            },
            {
            "firstName":"SHOPLIFTING BY ASPORTATION c266 \u00a730A",
            "lastName":"266\/30A\/A"
            },
            {
            "firstName":"SHOPLIFTING BY ASPORTATION, 2ND OFF. c266 \u00a730A",
            "lastName":"266\/30A\/B"
            },
            {
            "firstName":"SHOPLIFTING BY ASPORTATION, 3RD OFF. c266 \u00a730A",
            "lastName":"266\/30A\/C"
            },
            {
            "firstName":"SHOPLIFTING BY CONCEALING MDSE c266 \u00a730A",
            "lastName":"266\/30A\/D"
            },
            {
            "firstName":"SHOPLIFTING BY CONCEALING MDSE, 2ND OFF. c266 \u00a730A",
            "lastName":"266\/30A\/E"
            },
            {
            "firstName":"SHOPLIFTING BY CONCEALING MDSE, 3RD OFF. c266 \u00a730A",
            "lastName":"266\/30A\/F"
            },
            {
            "firstName":"SHOPLIFTING BY CONTAINER SWITCHING c266 \u00a730A",
            "lastName":"266\/30A\/J"
            },
            {
            "firstName":"SHOPLIFTING BY CONTAINER SWITCHING, 2ND c266 \u00a730A",
            "lastName":"266\/30A\/K"
            },
            {
            "firstName":"SHOPLIFTING BY CONTAINER SWITCHING, 3RD c266 \u00a730A",
            "lastName":"266\/30A\/L"
            },
            {
            "firstName":"SHOPLIFTING BY PRICE TAG TAMPERING c266 \u00a730A",
            "lastName":"266\/30A\/G"
            },
            {
            "firstName":"SHOPLIFTING BY PRICE TAG TAMPERING, 2ND c266 \u00a730A",
            "lastName":"266\/30A\/H"
            },
            {
            "firstName":"SHOPLIFTING BY PRICE TAG TAMPERING, 3RD c266 \u00a730A",
            "lastName":"266\/30A\/I"
            },
            {
            "firstName":"SHOPLIFTING BY RECORDING FALSE VALUE c266 \u00a730A",
            "lastName":"266\/30A\/M"
            },
            {
            "firstName":"SHOPLIFTING BY RECORDING FALSE VALUE,3RD c266 \u00a730A",
            "lastName":"266\/30A\/O"
            },
            {
            "firstName":"SHOPLIFTING OF SHOPPING CART c266 \u00a730A",
            "lastName":"266\/30A\/P"
            },
            {
            "firstName":"SHOPLIFTING, 3RD AND SUBSQ OFF; UNDER $100.00 c. 266 s. 30A",
            "lastName":"266.30A"
            },
            {
            "firstName":"SHOPLIFTING; OVER $100.00 c. 266 s. 30A",
            "lastName":"266.30A"
            },
            {
            "firstName":"SHOTGUN, POSSESS c269 \u00a710(h)",
            "lastName":"269\/10\/S1"
            },
            {
            "firstName":"SHOTGUN, POSSESS SAWED-OFF c269 \u00a710(c)",
            "lastName":"269\/10\/W"
            },
            {
            "firstName":"SHOTGUN, POSSESS SAWED-OFF c269 \u00a710(c)",
            "lastName":"269\/10\/S"
            },
            {
            "firstName":"SHOTGUN, POSSESS SAWED-OFF, 2ND OFF. c269 \u00a710(c) & (d)",
            "lastName":"269\/10\/T"
            },
            {
            "firstName":"SHOTGUN, POSSESS SAWED-OFF, 2ND OFF. c269 \u00a710(c) & (d)",
            "lastName":"269\/10\/X"
            },
            {
            "firstName":"SHOTGUN, POSSESS SAWED-OFF, 3RD OFF. c269 \u00a710(c) & (d)",
            "lastName":"269\/10\/U"
            },
            {
            "firstName":"SHOTGUN, POSSESS SAWED-OFF, 4TH OFF. c269 \u00a710(c) & (d)",
            "lastName":"269\/10\/V"
            },
            {
            "firstName":"SHOTGUN\/RIFLE IN MV\/PLANE\/BOAT, LOADED c131 \u00a763",
            "lastName":"131\/63"
            },
            {
            "firstName":"SHPLFTG BY CONCEALG MERCH.",
            "lastName":"266\/30A"
            },
            {
            "firstName":"SIDEWALK, SELL ON PUBLIC c93 \u00a740",
            "lastName":"93\/40"
            },
            {
            "firstName":"SIGHTSEEING TOURS BY AUTOMOBILE; UNLICENSED c. 159A App. s. 1-6",
            "lastName":"159A App..1-6"
            },
            {
            "firstName":"SIGN NAME, MV OPERATOR REFUSE c90 \u00a725",
            "lastName":"90\/25\/C"
            },
            {
            "firstName":"SIGNAL, FAIL TO * c90 \u00a714B",
            "lastName":"90\/14B"
            },
            {
            "firstName":"SIGNATURE, OBTAINING BY FALSE PRETENSE c. 266 s. 31",
            "lastName":"266.31"
            },
            {
            "firstName":"SIGNATURE, OBTAINING BY FALSE PRETENSE c266 \u00a731",
            "lastName":"266\/31"
            },
            {
            "firstName":"SILENCER, SELL\/USE\/POSSESS FIREARM c. 269 s. 10A",
            "lastName":"269.10A"
            },
            {
            "firstName":"SILENCER, SELL\/USE\/POSSESS FIREARM c269 \u00a710A",
            "lastName":"269\/10A"
            },
            {
            "firstName":"SLOW, FAIL TO * c90 \u00a714",
            "lastName":"90\/14\/A"
            },
            {
            "firstName":"SLUGS, MANUFACTURE\/SELL FOR COIN MACHINES c266 \u00a775B",
            "lastName":"266\/75B"
            },
            {
            "firstName":"SMALL LOANS, UNLICENSED c140 \u00a7110",
            "lastName":"140\/110"
            },
            {
            "firstName":"SMOKE DETECTOR VIOLATION c148 \u00a726E",
            "lastName":"148\/26E"
            },
            {
            "firstName":"SMOKING ON MBTA c. 272 s. 43A",
            "lastName":"272.43A"
            },
            {
            "firstName":"SMOKING ON MBTA c272 \u00a743A",
            "lastName":"272\/43A\/A"
            },
            {
            "firstName":"SNOW VEH\u00bfPRIVATE PROPERTY, ON * c90B \u00a726",
            "lastName":"90B\/26\/J"
            },
            {
            "firstName":"SNOW\/ICE, VIOL MUNIC BY-LAW ON REMOVING c85 \u00a75",
            "lastName":"85\/5"
            },
            {
            "firstName":"SNOW\/REC VEH,PUBLIC WAY, ON c. 90B s. 25",
            "lastName":"90B.25"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfEQUIPMENT VIOLATION * 323 CMR \u00a73.07",
            "lastName":"323CMR307"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfEQUIPMENT VIOLATION * c90B \u00a724",
            "lastName":"90B\/24\/A"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfFIREARM, OP WHILE CARRY * c90B \u00a726",
            "lastName":"90B\/26\/A"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfGROWING STOCK, DAMAGE * c90B \u00a726",
            "lastName":"90B\/26\/B"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfHELMET VIOLATION * c90B \u00a726",
            "lastName":"90B\/26\/C"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfNOISE VIOLATION * c90B \u00a724",
            "lastName":"90B\/24\/C"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfNUMBER PLATE VIOLATION * 323 CMR \u00a73.05",
            "lastName":"323CMR305"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfPUBLIC WAY, ON c90B \u00a725",
            "lastName":"90B\/25"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfREGISTRATION, FL PRODUCE * c90B \u00a722",
            "lastName":"90B\/22\/B"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfSTOP FOR POLICE, FAIL * c90B \u00a732",
            "lastName":"90B\/32"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfUNDER 14 OPERATE UNSUPERVSD c90B \u00a726",
            "lastName":"90B\/26\/H"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfUNREGISTERED * c90B \u00a721",
            "lastName":"90B\/21"
            },
            {
            "firstName":"SNOW\/REC VEH\u00bfUNSAFE OPERATION * c90B \u00a726",
            "lastName":"90B\/26\/F"
            },
            {
            "firstName":"SNOW\/REC VEHICLE VIOLATION * 323 CMR \u00a73.03",
            "lastName":"323CMR303"
            },
            {
            "firstName":"SODOMY c272 \u00a734",
            "lastName":"272\/34\/A"
            },
            {
            "firstName":"SOLICIT FROM PERSONS IN MOTOR VEHICLES c85 \u00a717A",
            "lastName":"85\/17A\/A"
            },
            {
            "firstName":"SOLICIT TO COMMIT CRIME PUNISHABLE BY IMPRISON LIFE c274 \u00a78\/A",
            "lastName":"274\/8\/A"
            },
            {
            "firstName":"SOLICIT TO COMMIT FELONY (Common Law)",
            "lastName":"COMLAW6"
            },
            {
            "firstName":"SOLICITING\/SECURING PROSTITUTE OR SEX FOR FEE",
            "lastName":"2CHL13\/A"
            },
            {
            "firstName":"SPECIAL NEEDS STUDENTS VEH FL ID OWNER * c90 \u00a77CC",
            "lastName":"90\/7CC"
            },
            {
            "firstName":"SPEEDING",
            "lastName":"90\/18"
            },
            {
            "firstName":"SPEEDING",
            "lastName":"90\/17"
            },
            {
            "firstName":"SPEEDING * c90 \u00a717",
            "lastName":"90\/17\/A"
            },
            {
            "firstName":"SPEEDING c. 90 s. 17",
            "lastName":"90. 17"
            },
            {
            "firstName":"SPEEDING IN VIOL SPECIAL REGULATION * c90 \u00a718",
            "lastName":"90\/18\/A"
            },
            {
            "firstName":"SPEEDING ON COUNTY BRIDGE VIOL BY-LAW * c85 \u00a720",
            "lastName":"85\/20"
            },
            {
            "firstName":"SPEEDING RATE OF SPEED GREATER THAN WAS REASONABLE AND PROPER  c90 \u00a7 17",
            "lastName":"90\/17\/e"
            },
            {
            "firstName":"SPEEDING WHILE OVERWEIGHT VIOL PERMIT * c90 \u00a717",
            "lastName":"90\/17\/B"
            },
            {
            "firstName":"SPITTING IN PUBLIC PLACE c270 \u00a714",
            "lastName":"270\/14"
            },
            {
            "firstName":"SPORTING EVENT, THROW OBJECT AT c. 265 s. 36",
            "lastName":"265.36"
            },
            {
            "firstName":"SPORTING EVENT, THROW OBJECT AT c265 \u00a736",
            "lastName":"265\/36"
            },
            {
            "firstName":"SPRINKLER SYSTEM VIOL c148 \u00a726B",
            "lastName":"148\/26B"
            },
            {
            "firstName":"SPRINKLER SYSTEM VIOL, HIGH RISE c148 \u00a726A",
            "lastName":"148\/26A"
            },
            {
            "firstName":"SPRINKLER SYSTEM VIOL, MULTIPLE DWELL c148 \u00a726I",
            "lastName":"148\/26I"
            },
            {
            "firstName":"SPRINKLER SYSTEM, DISCONNECT c148 \u00a727A",
            "lastName":"148\/27A"
            },
            {
            "firstName":"SPRINKLER SYSTEM, FAIL INSTALL c148 \u00a727",
            "lastName":"148\/27"
            },
            {
            "firstName":"STALKING",
            "lastName":"12321|265:43"
            },
            {
            "firstName":"STALKING c. 265 s. 43(a)",
            "lastName":"265.43(a)"
            },
            {
            "firstName":"STALKING c265 \u00a743(a)",
            "lastName":"265\/43\/A"
            },
            {
            "firstName":"STALKING IN VIOL OF RESTRAINING ORDER c. 265 s. 43(b)",
            "lastName":"265.43(b)"
            },
            {
            "firstName":"STALKING IN VIOL OF RESTRAINING ORDER c265 \u00a743(b)",
            "lastName":"265\/43\/B"
            },
            {
            "firstName":"STALKING, SUBSQ. OFF. c. 265 s. 43(c)",
            "lastName":"265.43(c)"
            },
            {
            "firstName":"STALKING, SUBSQ.OFF. c265 \u00a743(c)",
            "lastName":"265\/43\/D"
            },
            {
            "firstName":"STATE BUILDING, DAMAGE c. 266 s. 96",
            "lastName":"266.96"
            },
            {
            "firstName":"STATE BUILDING, VANDALIZE c266 \u00a796",
            "lastName":"266\/96"
            },
            {
            "firstName":"STATE HWAY WRONG WAY  * 720 CMR \u00a79.05",
            "lastName":"720CMR905"
            },
            {
            "firstName":"STATE HWAY\u00bfCLOSED TO TRAVEL, MV WHERE * c85 \u00a72E",
            "lastName":"85\/2E\/A"
            },
            {
            "firstName":"STATE HWAY\u00bfCLOSED TO TRAVEL, PERSON WHERE c85 \u00a72E",
            "lastName":"85\/2E\/B"
            },
            {
            "firstName":"STATE HWAY\u00bfGUBERNATORIAL BY-LAW VIOL * c85 \u00a723",
            "lastName":"85\/23"
            },
            {
            "firstName":"STATE HWAY\u00bfHAZARDOUS MAT TRANSP VIOL * 720 CMR \u00a78.03 & \u00a78.04",
            "lastName":"720CMR803"
            },
            {
            "firstName":"STATE HWAY\u00bfIMPACT TRAFFIC ON c81 \u00a721",
            "lastName":"81\/21\/B"
            },
            {
            "firstName":"STATE HWAY\u00bfLEFT LANE RESTRICTION VIOL * 720 CMR \u00a79.08(5)(b)",
            "lastName":"720CMR908\/G"
            },
            {
            "firstName":"STATE HWAY\u00bfPARKING * 720 CMR \u00a79.03",
            "lastName":"720CMR903"
            },
            {
            "firstName":"STATE HWAY\u00bfPEDESTRIAN VIOLATION 720 CMR \u00a79.09",
            "lastName":"720CMR909\/A"
            },
            {
            "firstName":"STATE HWAY\u00bfRAMP, BACK ON\/OFF * 720 CMR \u00a79.08",
            "lastName":"720CMR908\/C"
            },
            {
            "firstName":"STATE HWAY\u00bfSIGNAL\/SIGN\/MARKINGS VIOL * 720 CMR \u00a79.06",
            "lastName":"720CMR906\/A"
            },
            {
            "firstName":"STATE HWAY\u00bfSOUTH BOSTON HAUL ROAD VIOLATION * 720 CMR \u00a79.08(6)(a)",
            "lastName":"720CMR908\/H"
            },
            {
            "firstName":"STATE HWAY\u00bfTRAFFIC VIOLATION * 720 CMR \u00a79.06",
            "lastName":"720CMR906\/B"
            },
            {
            "firstName":"STATE HWAY\u00bfTRAFFIC VIOLATION * 720 CMR \u00a79.07",
            "lastName":"720CMR907"
            },
            {
            "firstName":"STATE SANITARY CODE MEDICAL WASTE VIOL c. 111 s. 127A",
            "lastName":"111.127A"
            },
            {
            "firstName":"STATE SANITARY CODE VIOLATION c111 \u00a7127A",
            "lastName":"111\/127A\/B"
            },
            {
            "firstName":"STOLEN MV, FAIL REPORT RECOVERY OF c90D \u00a733",
            "lastName":"90D\/33"
            },
            {
            "firstName":"STOLEN PROPERTY, REFUSE RETURN c. 266 s. 21",
            "lastName":"266.21"
            },
            {
            "firstName":"STOLEN PROPERTY, REFUSE RETURN c266 \u00a721",
            "lastName":"266\/21"
            },
            {
            "firstName":"STOLEN VALOR, FRAUD REPRESENTATION MILITARY VETERAN c272\/106",
            "lastName":"272\/106\/A"
            },
            {
            "firstName":"STOP FOR POLICE, FAIL c90 \u00a725",
            "lastName":"90\/25\/D"
            },
            {
            "firstName":"STOP SIGN VIOLATION",
            "lastName":"89\/9\/B"
            },
            {
            "firstName":"STOP SIGN, FAILURE TO STOP OR RED SIGNAL VIOLATION c. 89 s. 9",
            "lastName":"c. 89 s. 9"
            },
            {
            "firstName":"STOP\/YIELD, FAIL TO * c89 \u00a79",
            "lastName":"89\/9"
            },
            {
            "firstName":"STRANGULATION OR SUFFOCATION c265 \u00a715D(a)",
            "lastName":"265\/15D\/A"
            },
            {
            "firstName":"STRANGULATION OR SUFFOCATION, PREGNANT VICTIM c265 \u00a715D(c)",
            "lastName":"265\/15D\/C"
            },
            {
            "firstName":"STRANGULATION OR SUFFOCATION, SERIOUS BODILY INJURY c265 \u00a715D(a)",
            "lastName":"265\/15D\/B"
            },
            {
            "firstName":"STRANGULATION OR SUFFOCATION, SUBSQ.OFF c265 \u00a715Dc",
            "lastName":"265\/15D\/D"
            },
            {
            "firstName":"STREETCAR DIRECTOR VIOLATION c. 161 s. 31",
            "lastName":"161.31"
            },
            {
            "firstName":"STREETCAR FAIL STOP FOR FIRE APPARATUS c89 \u00a76A",
            "lastName":"89\/6A"
            },
            {
            "firstName":"STREETCAR OBSTRUCT PUBLIC WAY c161 \u00a796",
            "lastName":"161\/96"
            },
            {
            "firstName":"STREETCAR OBSTRUCT; ENDANGER LIFE AND SAFETY OF OTHERS c. 161 s. 94",
            "lastName":"161.94"
            },
            {
            "firstName":"STREETCAR TRANSFER TICKET, MISUSE c161 \u00a7113",
            "lastName":"161\/113"
            },
            {
            "firstName":"STREETCAR, OBSTRUCT c. 161 s. 94",
            "lastName":"161.94"
            },
            {
            "firstName":"STREETCAR, OBSTRUCT c161 \u00a794",
            "lastName":"161\/94\/A"
            },
            {
            "firstName":"STREETWALKER, COMMON c. 272 s. 53",
            "lastName":"272.53"
            },
            {
            "firstName":"STREETWALKER, COMMON c272 \u00a753",
            "lastName":"272\/53\/C"
            },
            {
            "firstName":"STRIPED BASS TAKEN NOT BY ANGLING c130 \u00a7100B",
            "lastName":"130\/100B\/A"
            },
            {
            "firstName":"STUDENT MOTOR VEH REGISTRATION VIOL * c90 \u00a73",
            "lastName":"90\/3\/B"
            },
            {
            "firstName":"SUPPORT CHILD, LEAVE COMM WITHOUT c273 \u00a71(2)",
            "lastName":"273\/1\/D"
            },
            {
            "firstName":"SUPPORT ORDER, FAIL COMPLY WITH c273 \u00a71(4)",
            "lastName":"273\/1\/E"
            },
            {
            "firstName":"SUPPORT SPOUSE, LEAVE COMM WITHOUT c273 \u00a71(2)",
            "lastName":"273\/1\/F"
            },
            {
            "firstName":"SUPPORT, ABANDON CHILD WITHOUT c273 \u00a71(1)",
            "lastName":"273\/1\/A"
            },
            {
            "firstName":"SYNTHETIC CANNABINOID, POSSESSION OR SALE OF c16 \u00a759.3",
            "lastName":"16BOS59\/A"
            },
            {
            "firstName":"TAGGING PROPERTY c. 266 s. 126B",
            "lastName":"266.126B"
            },
            {
            "firstName":"TAGGING PROPERTY c266 \u00a7126B",
            "lastName":"266\/126B"
            },
            {
            "firstName":"TASK FORCE ARREST",
            "lastName":"61414|"
            },
            {
            "firstName":"TATTOOING c265 \u00a734",
            "lastName":"265\/34"
            },
            {
            "firstName":"TAX COLLECTOR, IMPEDE BY THREATS c62C \u00a773(h)",
            "lastName":"62C\/73\/D"
            },
            {
            "firstName":"TAX RECORDS\/INFO, FAIL PROVIDE c62C \u00a773(c)",
            "lastName":"62C\/73\/G"
            },
            {
            "firstName":"TAX RETURN, AID FALSE c62C \u00a773(f)(2)",
            "lastName":"62C\/73\/H"
            },
            {
            "firstName":"TAX RETURN, FAIL FILE c62C \u00a773(c)",
            "lastName":"62C\/73\/I"
            },
            {
            "firstName":"TAX RETURN, FALSE c62C \u00a773(g)",
            "lastName":"62C\/73\/J"
            },
            {
            "firstName":"TAX RETURN, FALSE VERIFIED c62C \u00a773(f)(1)",
            "lastName":"62C\/73\/K"
            },
            {
            "firstName":"TAX, ATTEMPT TO EVADE c62C \u00a773(a)",
            "lastName":"62C\/73\/N"
            },
            {
            "firstName":"TAX, EVADE c62C \u00a773(c)",
            "lastName":"62C\/73\/P"
            },
            {
            "firstName":"TAX, FAIL COLLECT OR PAY OVER c62C \u00a773(b)",
            "lastName":"62C\/73\/Q"
            },
            {
            "firstName":"TAXI FARE, ATTEMPT TO EVADE c159A \u00a716",
            "lastName":"159A\/16\/A"
            },
            {
            "firstName":"TAXI FARE, ATTEMPT TO EVADE c159A \u00a716A",
            "lastName":"159\/16\/A"
            },
            {
            "firstName":"TAXI FARE, EVADE c159A \u00a716",
            "lastName":"159A\/16\/B"
            },
            {
            "firstName":"TAXI FARE, EVADING",
            "lastName":"159A\/16"
            },
            {
            "firstName":"TAXI RECORDKEEPING VIOLATION c159A \u00a710",
            "lastName":"159A\/10\/A"
            },
            {
            "firstName":"TAXI VIOLATION c159A \u00a715",
            "lastName":"159A\/15\/A"
            },
            {
            "firstName":"TAXI VIOLATION, SUBSQ.OFF. c159A \u00a715",
            "lastName":"159A\/15\/B"
            },
            {
            "firstName":"TEAR GAS\/MACE, USE IN CRIME c. 269 s. 10C",
            "lastName":"269.10C"
            },
            {
            "firstName":"TEAR GAS\/MACE, USE IN CRIME c269 \u00a710C",
            "lastName":"269\/10C"
            },
            {
            "firstName":"TELEPHONE CALLS, ANNOYING c269 \u00a714A",
            "lastName":"269\/14A\/A"
            },
            {
            "firstName":"TELEPHONE CALLS, ANNOYING OR OBSCENE c. 269 s. 14A",
            "lastName":"269.14A"
            },
            {
            "firstName":"TELEPHONE CALLS, OBSCENE c269 \u00a714A",
            "lastName":"269\/14A\/B"
            },
            {
            "firstName":"TELEPHONE CREDIT CARD SYSTEM, PUBLISH c266 \u00a737D",
            "lastName":"266\/37D"
            },
            {
            "firstName":"TELEPHONE DEVICE, UNLAWFUL c. 166 s. 42B",
            "lastName":"166.42B"
            },
            {
            "firstName":"TELEPHONE FOR GAMING, USE c. 271 s. 17A",
            "lastName":"271.17A"
            },
            {
            "firstName":"TELEPHONE FOR GAMING, USE c271 \u00a717A",
            "lastName":"271\/17A\/A"
            },
            {
            "firstName":"TELEPHONE PARTY LINE, MISUSE c166 \u00a715C",
            "lastName":"166\/15C"
            },
            {
            "firstName":"TELEPHONE SERVICE BY FRAUD -$5000, ATT c166 \u00a742A",
            "lastName":"166\/42A\/D"
            },
            {
            "firstName":"TELEPHONE SERVICE BY FRAUD -$5000,OBTAIN c166 \u00a742A",
            "lastName":"166\/42A\/C"
            },
            {
            "firstName":"TELEPHONE SERVICE BY FRAUD +$5000,OBTAIN c166 \u00a742A",
            "lastName":"166\/42A\/G"
            },
            {
            "firstName":"THIEF, COMMON & NOTORIOUS c. 266 s. 40",
            "lastName":"266.4"
            },
            {
            "firstName":"THIEF, COMMON & NOTORIOUS c266 \u00a740",
            "lastName":"266\/40"
            },
            {
            "firstName":"THREAT TO COMMIT CRIME c. 275 s. 2",
            "lastName":"275.2"
            },
            {
            "firstName":"THREAT TO COMMIT CRIME c275 \u00a72",
            "lastName":"275\/2"
            },
            {
            "firstName":"THREAT, BUSINESS c271 \u00a739(a)",
            "lastName":"271\/39\/B"
            },
            {
            "firstName":"THREATENED USE OR PRESENCE OF DEADLY DEVICE OR SUBSTANCE c269 \u00a714(c)",
            "lastName":"269\/14\/C"
            },
            {
            "firstName":"TICKET RESALE BY OWNER c140 \u00a7185A",
            "lastName":"140\/185A\/A"
            },
            {
            "firstName":"TICKET RESALE REGUL VIOLATION c140 \u00a7185E",
            "lastName":"140\/185E\/A"
            },
            {
            "firstName":"TICKET RESALE REGUL VIOLATION, 3RD AND SUBSQ. OFF. c. 140 s. 185E",
            "lastName":"140.185E"
            },
            {
            "firstName":"TICKET RESALE VIOLATION, 3RD AND SUBSQ. OFF. c. 140 s. 185A",
            "lastName":"140.185A"
            },
            {
            "firstName":"TICKET RESALE, UNLICENSED c140 \u00a7185A",
            "lastName":"140\/185A\/C"
            },
            {
            "firstName":"TICKET RESALE, UNLICENSED, 3RD OFF. c140 \u00a7185A",
            "lastName":"140\/185A\/D"
            },
            {
            "firstName":"TICKET SCALPING c140 \u00a7185D",
            "lastName":"140\/185D\/A"
            },
            {
            "firstName":"TICKET SCALPING, 3RD AND SUBSQ. OFF. c. 140 s. 185D",
            "lastName":"140.185D"
            },
            {
            "firstName":"TIDE WATER DREDGING\/DUMPING VIOLATION c91 \u00a754 & \u00a755",
            "lastName":"91\/54"
            },
            {
            "firstName":"TIMBER, WOOD AND SHRUBS, CUT OR DESTROY c. 266 s. 113",
            "lastName":"266.113"
            },
            {
            "firstName":"TIRE OUTSIDE FENDER c90 \u00a719",
            "lastName":"90\/19\/B"
            },
            {
            "firstName":"TIRE TREAD DEPTH VIOLATION * c90 \u00a77Q",
            "lastName":"90\/7Q"
            },
            {
            "firstName":"TIRE WIDTH BY-LAW VIOLATION * c40 \u00a721(9)",
            "lastName":"40\/21\/H"
            },
            {
            "firstName":"TIRES, SELL NONCONFORM RETREAD c90 \u00a77M",
            "lastName":"90\/7M\/A"
            },
            {
            "firstName":"TITLE, ALLOW UNAUTH POSSESSION\/USE OF MV c90D \u00a732(b)",
            "lastName":"90D\/32\/A"
            },
            {
            "firstName":"TITLE, FALSE MV c90D \u00a732(a)",
            "lastName":"90D\/32\/B"
            },
            {
            "firstName":"TITLE, FALSE STATEMENT IN APPLIC FOR MV c90D \u00a732(a)",
            "lastName":"90D\/32\/C"
            },
            {
            "firstName":"TOBIN BRIDGE\u00bfHITCHHIKING\/LOITERING 740 CMR \u00a711.05(1)(b)",
            "lastName":"740CMR1105\/N"
            },
            {
            "firstName":"TOBIN BRIDGE\u00bfSPEEDING OVER POSTED LIMIT * 740 CMR \u00a711.05",
            "lastName":"740CMR1105\/A"
            },
            {
            "firstName":"TOBIN BRIDGE\u00bfSPEEDING OVER POSTED LIMIT * 740 CMR \u00a711.06(1)(h)",
            "lastName":"740CMR1106\/A"
            },
            {
            "firstName":"TOBIN BRIDGE\u00bfTOLL, EVADE 740 CMR \u00a711.03",
            "lastName":"740CMR1103"
            },
            {
            "firstName":"TOBIN BRIDGE\u00bfTRAFFIC VIOLATION * 740 CMR \u00a711.06(1)(b)-(f) or (i)-(j)",
            "lastName":"740CMR1106\/B"
            },
            {
            "firstName":"TOOLS, LARCENY OF CONSTRUCTION c. 266 s. 27",
            "lastName":"266.27"
            },
            {
            "firstName":"TOOLS, LARCENY OF CONSTRUCTION c266 \u00a727",
            "lastName":"266\/27\/A"
            },
            {
            "firstName":"TOOLS, LARCENY OF CONSTRUCTION, SUBSQ. c266 \u00a727",
            "lastName":"266\/27\/B"
            },
            {
            "firstName":"TRADE SECRET, BUY\/SELL\/RECEIVE STOLEN c. 266 s. 60A",
            "lastName":"266.60A"
            },
            {
            "firstName":"TRADE SECRET, BUY\/SELL\/RECEIVE STOLEN c266 \u00a760A",
            "lastName":"266\/60A"
            },
            {
            "firstName":"TRADE SECRET, LARCENY OF c. 266 s. 30(4) ",
            "lastName":"266.30(4)"
            },
            {
            "firstName":"TRADE SECRET, LARCENY OF c266 \u00a730(4)",
            "lastName":"266\/30\/H"
            },
            {
            "firstName":"TRAFFIC IN COCAINE",
            "lastName":"94C\/32E"
            },
            {
            "firstName":"TRAFFICKING COCAINE SECOND OR SUBSEQUENT OFFENSE C.94C, \u00a732(E)(a)",
            "lastName":"94C\/32E\/A094C\/32E\/A0"
            },
            {
            "firstName":"TRAFFICKING PERSONS FOR SEXUAL SERVITUDE c. 265 s. 50",
            "lastName":"265\/50"
            },
            {
            "firstName":"TRAMP, THREATS BY c272 \u00a764",
            "lastName":"272\/64\/B"
            },
            {
            "firstName":"TRAMP, TRESPASS IN BUILDING BY c272 \u00a764",
            "lastName":"272\/64\/C"
            },
            {
            "firstName":"TRANSFER TICKET; MISUSE c. 161 s. 113",
            "lastName":"161.113"
            },
            {
            "firstName":"TRANSIENT VENDOR SPECIAL STATEMENT VIOL c. 101 s. 7",
            "lastName":"101.7"
            },
            {
            "firstName":"TRANSIENT VENDOR, UNLICENSED c. 101 s. 8",
            "lastName":"101.8"
            },
            {
            "firstName":"TRANSITIONAL ASSISTANCE, EMPLOYEE IN WELFARE FRAUD c. 118 s. 2 Note St. 1995 c.  5 s. 117",
            "lastName":"118.2 Note"
            },
            {
            "firstName":"TRANSPORT NETWORK, DRIVER USE ID OF ANOTHER OR MISREP ANOTHER c159A\/7\/D",
            "lastName":"159A\/7\/D"
            },
            {
            "firstName":"TRANSPORTATION OF UNLAWFULLY TAKEN FISH\/ANIMALS INTO OR OUT OF THE COMMONWEALTH c. 131 s. 85",
            "lastName":"131.85"
            },
            {
            "firstName":"TRASH, DUMP FROM MV +7 CU FT c270 \u00a716",
            "lastName":"270\/16\/G"
            },
            {
            "firstName":"TRASH, LITTER c270 \u00a716",
            "lastName":"270\/16\/A"
            },
            {
            "firstName":"TRASH, LITTER FROM MV c270 \u00a716",
            "lastName":"270\/16\/E"
            },
            {
            "firstName":"TREASON c. 264 s. 2",
            "lastName":"264.2"
            },
            {
            "firstName":"TREE BY-LAW VIOL, PUBLIC SHADE c87 \u00a72",
            "lastName":"87\/2"
            },
            {
            "firstName":"TREE\/SHRUB, WANTONLY INJURE PUBLIC c87 \u00a712",
            "lastName":"87\/12"
            },
            {
            "firstName":"TREES AND FENCES; MALICIOUS INJURY c. 266 s. 114",
            "lastName":"266.114"
            },
            {
            "firstName":"TREES, CUT\/DESTROY c266 \u00a7113",
            "lastName":"266\/113\/A"
            },
            {
            "firstName":"TREES, CUT\/DESTROY SUNDAY\/DISGUISE\/NIGHT c266 \u00a7113",
            "lastName":"266\/113\/B"
            },
            {
            "firstName":"TRESPASS c. 266 s. 120",
            "lastName":"266.12"
            },
            {
            "firstName":"TRESPASS c266 \u00a7120",
            "lastName":"266\/120"
            },
            {
            "firstName":"TRESPASS FOR TREE\/PLANT\/FRUIT c. 266 s. 117",
            "lastName":"266.117"
            },
            {
            "firstName":"TRESPASS NOTICE, VANDALIZE c266 \u00a7122",
            "lastName":"266\/122"
            },
            {
            "firstName":"TRESPASS ON STATE\/COUNTY PROPERTY c. 266 s. 123",
            "lastName":"266.123"
            },
            {
            "firstName":"TRESPASS ON STATE\/COUNTY PROPERTY c266 \u00a7123",
            "lastName":"266\/123"
            },
            {
            "firstName":"TRESPASS WITH FIREARM c. 266 s. 121",
            "lastName":"266.121"
            },
            {
            "firstName":"TRESPASS WITH FIREARM c266 \u00a7121",
            "lastName":"266\/121"
            },
            {
            "firstName":"TRESPASS WITH MOTOR VEHICLE * c266 \u00a7121A",
            "lastName":"266\/121A"
            },
            {
            "firstName":"TRESPASS WITH NON-MV VEHICLE  c266 \u00a7121A",
            "lastName":"266\/121A\/B"
            },
            {
            "firstName":"TRESPASSING",
            "lastName":"21129|266-120"
            },
            {
            "firstName":"TRUCK FAIL DISPLAY OWNER\u00bfS NAME * 540 CMR \u00a72.22(1)",
            "lastName":"540CMR222\/A"
            },
            {
            "firstName":"TRUCK, B&E FOR FELONY c266 \u00a720A",
            "lastName":"266\/20A\/A"
            },
            {
            "firstName":"TRUCK, B&E OR ENTER, FOR FELONY c. 266 s. 20A",
            "lastName":"266.20A"
            },
            {
            "firstName":"TRUCK, ENTER FOR FELONY c266 \u00a720A",
            "lastName":"266\/20A\/B"
            },
            {
            "firstName":"TRUCK, LARCENY FROM c. 266 s. 20B",
            "lastName":"266.20B"
            },
            {
            "firstName":"TRUCK, LARCENY FROM c266 \u00a720B",
            "lastName":"266\/20B"
            },
            {
            "firstName":"TURN, IMPROPER * c90 \u00a714",
            "lastName":"90\/14\/B"
            },
            {
            "firstName":"U.S. SIGNAL\/MONUMENT\/BLDG, VANDALIZE c1 \u00a710",
            "lastName":"10-Jan"
            },
            {
            "firstName":"UNARM ROBBERY",
            "lastName":"265\/19"
            },
            {
            "firstName":"UNAUTHORIZED ACCESS TO COMPUTER SYSTEM c. 266 s. 120F",
            "lastName":"266.120F"
            },
            {
            "firstName":"UNAUTHORIZED USE OF CREDIT CARDS c. 140D s. 27",
            "lastName":"140D.27"
            },
            {
            "firstName":"UNEMPLOYMENT COMP ADMIN, OBSTRUCT c151A \u00a747",
            "lastName":"151A\/47\/A"
            },
            {
            "firstName":"UNEMPLOYMENT COMP PAYMENT, BAD CHECK FOR c151A \u00a747A",
            "lastName":"151A\/47A"
            },
            {
            "firstName":"UNEMPLOYMENT COMP VIOLATION c151A \u00a747",
            "lastName":"151A\/47\/B"
            },
            {
            "firstName":"UNEMPLOYMENT COMP, EMPLOYER FAIL PAY c151A \u00a747",
            "lastName":"151A\/47\/D"
            },
            {
            "firstName":"UNEMPLOYMENT COMP, FALSE IDENTITY FOR c. 151A s. 47",
            "lastName":"151A.47"
            },
            {
            "firstName":"UNEMPLOYMENT COMP, FALSE IDENTITY FOR c151A \u00a747",
            "lastName":"151A\/47\/E"
            },
            {
            "firstName":"UNEMPLOYMENT COMP, FALSE STATEMENT FOR c. 151A s. 47",
            "lastName":"151A.47"
            },
            {
            "firstName":"UNEMPLOYMENT COMP, FALSE STATEMENT FOR c151A \u00a747",
            "lastName":"151A\/47\/F"
            },
            {
            "firstName":"UNEMPLOYMENT COMPENSATION; FALSE STATEMENT TO AVOID CONTRIBUTION TO c. 151A s. 47",
            "lastName":"151A.47"
            },
            {
            "firstName":"UNINSURED MOTOR VEHICLE c. 90 s. 34J",
            "lastName":"90.34J"
            },
            {
            "firstName":"UNINSURED MOTOR VEHICLE c90 \u00a734J",
            "lastName":"90\/34J"
            },
            {
            "firstName":"UNLAWFUL ASSEMBLY",
            "lastName":"269\/2"
            },
            {
            "firstName":"UNLAWFUL ASSEMBLY",
            "lastName":"12413|269-01"
            },
            {
            "firstName":"UNLAWFUL DEACTIVATION\/REMOVAL THEFT PROTECTION DEVICE c266 \u00a730B",
            "lastName":"266\/30B\/E"
            },
            {
            "firstName":"UNLAWFUL POSS. FIREARM, ON SCHOOL PROPERTY",
            "lastName":"12215|269-10 (J)"
            },
            {
            "firstName":"UNLAWFUL POSSESSION OF FIREARM",
            "lastName":"12214|269-10 (H)"
            },
            {
            "firstName":"UNLAWFULLY RECORDING NUDE OR PARTIALLY NUDE PERSON",
            "lastName":"272\/104\/A"
            },
            {
            "firstName":"UNLICENSED OPERATION OF MOTOR VEHICLE c. 90 s. 10a",
            "lastName":"90. 10a"
            },
            {
            "firstName":"UNLICENSED OPERATION OF MV c90 \u00a710",
            "lastName":"90\/10\/A"
            },
            {
            "firstName":"UNLICENSED OPERATOR, EMPLOY c90 \u00a712(a)",
            "lastName":"90\/12\/A"
            },
            {
            "firstName":"UNLICENSED\/SUSPENDED OPERATION OF MV, PERMIT c90 \u00a712",
            "lastName":"90\/12\/C"
            },
            {
            "firstName":"UNLICENSED\/SUSPENDED OPERATION OF MV, PERMIT, SUBSQ. OFF c90 \u00a712",
            "lastName":"90\/12\/D"
            },
            {
            "firstName":"UNNATURAL ACT c. 272 s. 35",
            "lastName":"272.35"
            },
            {
            "firstName":"UNNATURAL ACT c272 \u00a735",
            "lastName":"272\/35"
            },
            {
            "firstName":"UNNATURAL ACT WITH CHILD -16 c. 272 s. 35A",
            "lastName":"272.35A"
            },
            {
            "firstName":"UNNATURAL ACT WITH CHILD -16 c272 \u00a735A",
            "lastName":"272\/35A\/A"
            },
            {
            "firstName":"UNNATURAL AND LASCIVIOUS ACT",
            "lastName":"11515|265:22"
            },
            {
            "firstName":"UNREGISTERED MOTOR VEHICLE * c90 \u00a79",
            "lastName":"90\/9\/B"
            },
            {
            "firstName":"UNSAFE OPERATION OF MV * c90 \u00a713",
            "lastName":"90\/13\/A"
            },
            {
            "firstName":"USE MV WITHOUT AUTHORITY c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"USE MV WITHOUT AUTHORITY c90 \u00a724(2)(a)",
            "lastName":"90\/24\/P"
            },
            {
            "firstName":"USE MV WITHOUT AUTHORITY, 2ND OFF. c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"USE MV WITHOUT AUTHORITY, 2ND OFF. c90 \u00a724(2)(a)",
            "lastName":"90\/24\/Q"
            },
            {
            "firstName":"USE MV WITHOUT AUTHORITY, 3RD AND SUBSQ. OFF. c. 90 s. 24(2)(a)",
            "lastName":"90.24(2)(a)"
            },
            {
            "firstName":"USE MV WITHOUT AUTHORITY, 3RD OFF. c90 \u00a724(2)(a)",
            "lastName":"90\/24\/R"
            },
            {
            "firstName":"USE OF A FIREARM WHILE COMMITTING A FELONY",
            "lastName":"265\/18B"
            },
            {
            "firstName":"USED CAR DEALER FAIL KEEP REGISTER c140 \u00a762",
            "lastName":"140\/62"
            },
            {
            "firstName":"USED CAR REGULATIONS VIOLATION c140 \u00a760",
            "lastName":"140\/60"
            },
            {
            "firstName":"USED CAR SALES, UNLICENSED c. 140 s. 68",
            "lastName":"140.68"
            },
            {
            "firstName":"USED CAR SALES, UNLICENSED c140 \u00a768",
            "lastName":"140\/68"
            },
            {
            "firstName":"USING MOTOR VEHICLE WITHOUT AUTHORITY",
            "lastName":"31222|"
            },
            {
            "firstName":"USURY c. 271 s. 49(a)",
            "lastName":"271.49(a)"
            },
            {
            "firstName":"USURY c271 \u00a749(a) or (b)",
            "lastName":"271\/49\/A"
            },
            {
            "firstName":"UTILITY CO. PROPERTY, DAMAGE AT NIGHT c. 166 s. 38",
            "lastName":"166.38"
            },
            {
            "firstName":"UTILITY WIRES, CUT IN DAY c. 166 s. 40",
            "lastName":"166.4"
            },
            {
            "firstName":"UTTER A FORGERD INSTR",
            "lastName":"267\/5"
            },
            {
            "firstName":"UTTER COUNTERFEIT NOTE c267 \u00a710",
            "lastName":"267\/10\/A"
            },
            {
            "firstName":"UTTER COUNTERFEIT NOTE OR FALSE TRAVELLER'S CHECK c. 267 s. 10",
            "lastName":"267.1"
            },
            {
            "firstName":"UTTER FALSE CHECK c267 \u00a75",
            "lastName":"267\/5\/B"
            },
            {
            "firstName":"UTTER FALSE CHECK, INSTRUMENT, OR PROMISSORY NOTE c. 267 s. 5",
            "lastName":"267.5"
            },
            {
            "firstName":"UTTER FALSE ORDER FOR MONEY c267 \u00a75",
            "lastName":"267\/5\/D"
            },
            {
            "firstName":"UTTER FALSE TRAVELLER\u00bfS CHECK c267 \u00a710",
            "lastName":"267\/10\/B"
            },
            {
            "firstName":"UTTER FALSE WRITING c267 \u00a75",
            "lastName":"267\/5\/A"
            },
            {
            "firstName":"UTTER PROMISSORY NOTE FALSELY ENDORSED c267 \u00a75",
            "lastName":"267\/5\/C"
            },
            {
            "firstName":"UTTER WORTHLESS\/FALSE NOTE c267 \u00a728",
            "lastName":"267\/28"
            },
            {
            "firstName":"UTTERING (Common Law)",
            "lastName":"COMLAW9"
            },
            {
            "firstName":"VANDALIZE PROPERTY c266 \u00a7126A",
            "lastName":"266\/126A"
            },
            {
            "firstName":"VANDALIZE WAR\/VETERANS MEMORIAL c266 \u00a7126A",
            "lastName":"266\/126A\/B"
            },
            {
            "firstName":"VEHICLE ID NUMBER NOT DISPLAYED * c90 \u00a77R",
            "lastName":"90\/7R"
            },
            {
            "firstName":"VETERINARIAN, UNLICENSED c. 112 s. 59",
            "lastName":"112.59"
            },
            {
            "firstName":"VETERINARIAN, UNLICENSED c112 \u00a759",
            "lastName":"112\/59\/B"
            },
            {
            "firstName":"VIDEO RENTAL; RECORDS; VIOLATION c. 93 s. 106",
            "lastName":"93.106"
            },
            {
            "firstName":"VOTE UNLAWFULLY OR ATTEMPTS c. 56 s. 26",
            "lastName":"56.26"
            },
            {
            "firstName":"VOTE UNLAWFULLY, ATTEMPT TO c56 \u00a726",
            "lastName":"56\/26\/D"
            },
            {
            "firstName":"VOTE, ABET UNLAWFUL OR ATTEMPT c. 56 s. 28",
            "lastName":"56.28"
            },
            {
            "firstName":"WARRANT 0505CR001794 B&AMP;E BLDG DAY FOR FELONY",
            "lastName":"FDEFAULT"
            },
            {
            "firstName":"WARRANT 0607CR000093 USE MV WITHOUT AUTH",
            "lastName":"MSTRAIGHT"
            },
            {
            "firstName":"WARRANT ARREST",
            "lastName":"NONE"
            },
            {
            "firstName":"WARRANT FELONY DEFAULT - DOCKET &AMP; CHG IN NARRATIVE",
            "lastName":"FDEFAULT"
            },
            {
            "firstName":"WARRANT FELONY STRAIGHT- DOCKET &AMP; CHG IN NARRATIV",
            "lastName":"FSTRAIGHT"
            },
            {
            "firstName":"WARRANT MISDEMEANOR DEFAULT - DOCKET &AMP; CHG IN NARR",
            "lastName":"MDEFAULT"
            },
            {
            "firstName":"WARRANT MISDEMENAOR STRAIGHT - DOCKET &AMP; CHG IN NAR",
            "lastName":"MSTRAIGHT"
            },
            {
            "firstName":"WATER POLLUTION VIOLATION c21 \u00a742",
            "lastName":"21\/42\/B"
            },
            {
            "firstName":"WATER SKIS\/SURFBOARD, NEGLIGENT USE OF c90B \u00a78(b)",
            "lastName":"90B\/8\/F"
            },
            {
            "firstName":"WATERFRONT SAFETY VIOLATION c149 \u00a718I",
            "lastName":"149\/18I"
            },
            {
            "firstName":"WATERS, POLLUTE COMMONWEALTH c21 \u00a742",
            "lastName":"21\/42\/D"
            },
            {
            "firstName":"WEIGHED, REFUSAL TO BE * c90 \u00a719A",
            "lastName":"90\/19A\/C"
            },
            {
            "firstName":"WEIGHT OR WEIGHT CERTIFICATE, VIOLATIONS c. 90 s. 19D",
            "lastName":"90.19D"
            },
            {
            "firstName":"WEIGHT VIOLATION * c90 \u00a719A & \u00a720",
            "lastName":"90\/19A\/A"
            },
            {
            "firstName":"WEIGHT VIOLATION ON BRIDGE * c85 \u00a734",
            "lastName":"85\/34"
            },
            {
            "firstName":"WEIGHT VIOLATION ON STATE HWAY * c85 \u00a730",
            "lastName":"85\/30\/C"
            },
            {
            "firstName":"WILL, STEAL\/DESTROY\/CONCEAL c266 \u00a739",
            "lastName":"266\/39"
            },
            {
            "firstName":"WINDOW OBSTRUCTED\/NONTRANSPARENT * c90 \u00a79D",
            "lastName":"90\/9D"
            },
            {
            "firstName":"WIRETAP, DISCLOSE CONTENTS OF c272 \u00a799(C)(3) or (4)",
            "lastName":"272\/99\/A"
            },
            {
            "firstName":"WIRETAP, DISCLOSE CONTENTS OF, ATTEMPT c272 \u00a799(C)(3) or (4)",
            "lastName":"272\/99\/B"
            },
            {
            "firstName":"WIRETAP, POSSESS DEVICE FOR c272 \u00a799(C)(5)",
            "lastName":"272\/99\/C"
            },
            {
            "firstName":"WIRETAP, UNLAWFUL c272 \u00a799(C)(1)",
            "lastName":"272\/99\/F"
            },
            {
            "firstName":"WIRETAP, UNLAWFUL OR ATTEMPT c. 272 s. 99(c)(1)",
            "lastName":"272.99(c)(1)"
            },
            {
            "firstName":"WIRETAP, UNLAWFUL, ATTEMPT c272 \u00a799(C)(1)",
            "lastName":"272\/99\/G"
            },
            {
            "firstName":"WITNESS ACCEPT\/SOLICIT BRIBE c268A \u00a72(d)",
            "lastName":"268A\/2\/C"
            },
            {
            "firstName":"WITNESS FAIL TO APPEAR IN CRIMINAL CASE c. 233 s. 5",
            "lastName":"233.5"
            },
            {
            "firstName":"WITNESS FEE, OFFICER ACCEPT IMPROPER c262 \u00a750",
            "lastName":"262\/50"
            },
            {
            "firstName":"WITNESS, BRIBE c268A \u00a72(c)",
            "lastName":"268A\/2\/D"
            },
            {
            "firstName":"WITNESS, EMPLOYER PENALIZE\/THREATEN c258B \u00a73(l)",
            "lastName":"258B\/3"
            },
            {
            "firstName":"WITNESS, INTIMIDATE c268 \u00a713B",
            "lastName":"268\/13B\/A"
            },
            {
            "firstName":"WITNESS, RETALIATE AGAINST c268 \u00a713B",
            "lastName":"268\/13B\/B"
            },
            {
            "firstName":"WITNESS\/JUROR\/POLICE\/COURT OFF, INTIMIDATE AGGRAVATED c268 \u00a713B",
            "lastName":"268\/13B\/D"
            },
            {
            "firstName":"WITNESS\/JUROR\/POLICE\/COURT OFF, INTIMIDATE c268 \u00a713B",
            "lastName":"268\/13B\/A1"
            },
            {
            "firstName":"WORKERS COMP CLAIMS, ENCOURAGE c. 152 s. 14",
            "lastName":"152.14"
            },
            {
            "firstName":"WORKERS COMP FRAUD c152 \u00a714",
            "lastName":"152\/14\/A"
            },
            {
            "firstName":"WORKERS COMP, EMPLOYER FAIL HAVE c152 \u00a725C",
            "lastName":"152\/25C"
            },
            {
            "firstName":"YAR\u00bfLITTERING  Yarmouth By-Laws c97 \u00a71",
            "lastName":"97YAR1"
            },
            {
            "firstName":"YIELD AT INTERSECTION, FAIL * c89 \u00a78",
            "lastName":"89\/8"
            }
        ]
        returnValue = []
        for selection in item.split(","):
            ds=dataSource[int(selection)+1]
            returnValue.append(ds['firstName']+' '+ds['lastName'])
        return returnValue