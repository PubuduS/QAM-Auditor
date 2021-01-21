import sys
import chilkat

rest = chilkat.CkRest()

#  URL: http://10.0.50.125/probe/core/data.xml?
bTls = False
port = 80
bAutoReconnect = True
success = rest.Connect("10.0.50.125",port,bTls,bAutoReconnect)
if (success != True):
    print("ConnectFailReason: " + str(rest.get_ConnectFailReason()))
    print(rest.lastErrorText())
    sys.exit()

#  Note: The above code does not need to be repeatedly called for each REST request.
#  The rest object can be setup once, and then many requests can be sent.  Chilkat will automatically
#  reconnect within a FullRequest* method as needed.  It is only the very first connection that is explicitly
#  made via the Connect method.

#  Use this online tool to generate code from sample XML:
#  {{-https://tools.chilkat.io/xmlCreate.cshtml|||Generate Code to Create XML-}}

#  The following XML is sent in the request body.

#  <?xml version="1.0" encoding="utf-8"?>
#  <ewe mask="0x100" hw_type="4" br="BT" release="5.5.0-0">
#      <probe>
#          <core>
#              <qam1>
#                  <qam1Tunings>
#                      <qamTuningList xmlChildren="list" GreatestUsedTuningId="1" QamTuningVer="Jan  1 00:40:26">
#                          <preset name="201 MHz" tuningId="1" frequency="201.000M" chSpacing="8" symbolRate="5.360537 M" modulation="256" annex="1" etrThresholds="ATSC Default" pidThresholds="Default" serviceThresholds="Default" qamThresholds="Default" vbcThresholds="Default" extractThumbs="true" disable="false" referenceThresholds="[None]"/>
#                      </qamTuningList>
#                  </qam1Tunings>
#              </qam1>
#          </core>
#      </probe>
#  </ewe>
# 

xml = chilkat.CkXml()
xml.put_Tag("ewe")
xml.AddAttribute("mask","0x100")
xml.AddAttribute("hw_type","4")
xml.AddAttribute("br","BT")
xml.AddAttribute("release","5.5.0-0")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList",True,"xmlChildren","list")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList",True,"GreatestUsedTuningId","1")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList",True,"QamTuningVer","Jan  1 00:40:26")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"name","201 MHz")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"tuningId","1")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"frequency","201.000M")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"chSpacing","8")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"symbolRate","5.360537 M")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"modulation","256")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"annex","1")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"etrThresholds","ATSC Default")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"pidThresholds","Default")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"serviceThresholds","Default")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"qamThresholds","Default")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"vbcThresholds","Default")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"extractThumbs","true")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"disable","false")
xml.UpdateAttrAt("probe|core|qam1|qam1Tunings|qamTuningList|preset",True,"referenceThresholds","[None]")

sbRequestBody = chilkat.CkStringBuilder()
xml.GetXmlSb(sbRequestBody)

#  Send the request.
success = rest.SendReqSb("POST","/probe/core/data.xml",sbRequestBody)

#  Get the response header.
statusCode = rest.ReadResponseHeader()
if ((statusCode >= 200) and (statusCode <= 299)):
    respBodyStream = chilkat.CkStream()
    respBodyStream.put_SinkFile("out.html")
    success = rest.ReadRespBodyStream(respBodyStream,False)
else:
    #  The status code indicates an error. The response body contains error info.
    sbErrorResponse = chilkat.CkStringBuilder()
    success = rest.ReadRespSb(sbErrorResponse)
    if (success == True):
        print("Error response:")
        print(sbErrorResponse.getAsString())

if (success != True):
    print(rest.lastErrorText())
    sys.exit()
