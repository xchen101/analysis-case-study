#-- GAUDI jobOptions generated on Tue May 16 15:13:33 2017
#-- Contains event types : 
#--   21113001 - 64 files - 1022997 events - 216.34 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-124629 

#--  StepId : 124629 
#--  StepName : Merge14 for Sim08 
#--  ApplicationName : LHCb 
#--  ApplicationVersion : v35r4 
#--  OptionFiles : $APPCONFIGOPTS/Merging/CopyDST.py 
#--  DDDB : None 
#--  CONDDB : None 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : N 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000006_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000009_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000011_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000022_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000040_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000043_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000044_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000046_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000047_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000054_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000056_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000057_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000058_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000059_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000060_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000061_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000062_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000063_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000064_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000065_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00024300/0000/00024300_00000066_1.allstreams.dst'
], clear=True)