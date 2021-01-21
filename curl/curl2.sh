curl  -d "<?xml version=\"1.0\"?>
<ewe mask=\"0x100\" hw_type=\"4\" br=\"BT\" release=\"5.5.0-0\">
  <probe>
    <core>
      <qam1>
        <qam1Tunings>
          <qamTuningList xmlChildren=\"list\" GreatestUsedTuningId=\"1\" QamTuningVer=\"Jan  1 00:40:26\">
            <preset name=\"201 MHz\" tuningId=\"1\" frequency=\"201.000M\" chSpacing=\"8\" symbolRate=\"5.360537 M\" modulation=\"256\" annex=\"1\" etrThresholds=\"ATSC Default\" pidThresholds=\"Default\" serviceThresholds=\"Default\" qamThresholds=\"Default\" vbcThresholds=\"Default\" extractThumbs=\"true\" disable=\"false\" referenceThresholds=\"[None]\"></preset>
          </qamTuningList>
        </qam1Tunings>
      </qam1>
    </core>
  </probe>
</ewe>" -o out.html "http://10.0.50.125/probe/core/data.xml?"
