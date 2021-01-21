set LOC=C:\Users\pubuduw\Desktop\out.html
set ADDR=10.0.50.125
set FREQ=123

curl -s -d "<?xml version=\"1.0\"?>
<ewe mask=\"0x100\" hw_type=\"4\" br=\"BT\" release=\"5.5.0-0\">
  <probe>
    <core>
      <qam1>
        <qam1Tunings>
          <qamTuningList xmlChildren=\"list\" GreatestUsedTuningId=\"1\" QamTuningVer=\"Jan  1 00:40:26\">
            <preset name=\"%FREQ% MHz\" tuningId=\"1\" frequency=\"%FREQ%.000M\" chSpacing=\"8\" symbolRate=\"5.360537 M\" modulation=\"256\" annex=\"1\" etrThresholds=\"ATSC Default\" pidThresholds=\"Default\" serviceThresholds=\"Default\" qamThresholds=\"Default\" vbcThresholds=\"Default\" extractThumbs=\"true\" disable=\"false\" referenceThresholds=\"[None]\"></preset>
          </qamTuningList>
        </qam1Tunings>
      </qam1>
    </core>
  </probe>
</ewe>" -o out.html "http://%ADDR%/probe/core/data.xml?"
