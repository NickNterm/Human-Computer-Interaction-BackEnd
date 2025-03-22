API calls:
Get POIS/
list of pois

get Quiz/{POIid}/
list of 4 quiz of a poi random.

get reward/{POIid}/
get a reward for the poi you unlock

data structures:
POI:
lat: double
long: double
type: string
name: string
description: string
information: string << edw tha exoume html keimeno

Question
poi: ForeignKey
question: string
option1: string
option2: string
option3: string
answer: string

Rewards
poi: ForeignKey
title: string
description: string
code: string
