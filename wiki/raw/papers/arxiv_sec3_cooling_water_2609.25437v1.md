# Data center cooling choices shift water impacts across the grid: An integrated water-energy model for sustainable data center development
**arXiv ID:** 2609.25437v1
**Source File:** arxiv_sec3_cooling_water_2609.25437v1.pdf

## Page 1

Data Center Cooling Choices Shift Water Impacts Across the Grid:
An Integrated Water-Energy Model for Sustainable Data Center
Development
Garrett Alston
galston@umich.edu
Department of Civil and
Environmental Engineering,
University of Michigan
Ann Arbor, Michigan, USA
Nancy Love
nglove@umich.edu
Department of Civil and
Environmental Engineering,
University of Michigan
Ann Arbor, Michigan, USA
Rabab Haider
rababh@umich.edu
Department of Civil and
Environmental Engineering,
University of Michigan
Ann Arbor, Michigan, USA
Abstract
Data centers are being developed at an unprecedented pace, yet
their energy and water impacts, and the spatial and temporal distri-
bution of these impacts, remain poorly characterized. Data centers
consume water for cooling (direct) and through electricity genera-
tion (indirect). Decisions on siting and cooling technology result in
water–energy trade-offs that extend impacts beyond the facility’s
location. Existing assessment frameworks rely on facility efficiency
metrics and average grid water intensity factors, suppressing the
temporal impacts of data center load and generation availability.
They also attribute indirect consumption to the facility’s location
rather than to the generators (and corresponding hydrologic re-
gions) that respond to the added load, misattributing the spatial
impacts of data center loads. To close this gap, we develop a com-
putational model of the data center–energy–water nexus that links
facility cooling and electricity demand with hourly economic dis-
patch, generator-level water consumption, and monthly subbasin
depletion. Built on open-source data, the model resolves where and
when water is consumed, and where this consumption compounds
existing water risk or creates new risk. We apply the model to
cooling technology selection and to proposed developments in the
state of Michigan. Air-cooled data centers nearly halve total water
consumption relative to evaporative cooling, but increase electricity
demand and raise indirect water consumption by roughly one-third,
shifting the water footprint from the facility to generators on the
grid. Indirect water intensity also varies by approximately 50%
across months with the generators supplying the added load. Map-
ping these changes to subbasins reveals depletion increases beyond
the data center sites, in regions that facility-level reporting may
overlook. These results show that data center water and energy
impacts cannot be assessed in isolation, motivating the need for in-
tegrated modeling to inform siting, design, and reporting practices.
Keywords
data centers, water–energy nexus, water risk, sustainable comput-
ing, integrated system models
1
Introduction
The exponential growth of data centers is increasing electricity
demand worldwide, with continued expansion and increased con-
sumption expected as computing workloads and digital services
grow [8]. The United States accounts for the largest share of global
data center electricity consumption [8], with U.S. facilities consum-
ing an estimated 192 TWh in 2024, accounting for 4.7% of national
electricity consumption [23]. Data centers also consume substantial
quantities of water: Scope 1 or direct consumption is the on-site wa-
ter used at the facility, primarily for cooling; and Scope 2 or indirect
consumption is the off-site water used at the electricity generation
facilities to power the data center [14]. Critically, Scope 2 consump-
tion links energy and water impacts: decisions around facility siting,
cooling technology selection, and energy supply result in tradeoffs
across the water–energy nexus, and across spatial and temporal
dimensions.
Cooling configurations that reduce direct water consumption
may increase electricity demand and the indirect water consump-
tion associated with electricity generation. Evaporative cooling
systems consume relatively large quantities of direct water and re-
quire less electricity to operate, whereas non-evaporative systems
consume relatively small quantities of direct water but require more
electricity [9]. The resulting environmental impact of a data center
cannot be inferred from metrics reporting direct water consumption
alone. The proposed integrated data center–energy–water model
combines three metrics. Power usage effectiveness (PUE) relates
total facility electricity to information technology (IT) electricity
used by servers, storage, and networking equipment. Water usage
effectiveness (WUE) relates site water use to IT electricity. Water
consumption intensity (WCI) relates the volume of water consumed
by a generator per unit of electricity generated. Together, these
three metrics determine the water impact of a data center facility:
the cooling configuration determines the WUE and PUE of the
facility, and can shift water consumption between the data center
and the generators responding to its electricity demand, which are
represented by the WCI.
Importantly, these impacts also vary temporally and spatially.
Cooling performance changes with computing load and climate
conditions, while electricity demand, renewable availability, and
generator dispatch vary throughout the year. Direct water consump-
tion occurs at the data center, while indirect water consumption
occurs at the generators responding to its demand, so the water
impacts can occur across different hydrologic regions [22]. Assess-
ing water risk requires a consistent way to measure water use
and assess subsequent impacts. Withdrawal is the total volume re-
moved from a water source, whereas consumption is the portion of
that withdrawal not returned to the immediate water environment
[12]. These two quantities support different risk indicators. Water
arXiv:2609.25437v1  [eess.SY]  21 Sep 2026

---

## Page 2

Alston et al.
stress is commonly represented by the ratio of water withdrawals
to available water, whereas water depletion is the ratio of consump-
tive water use to renewable available water [4]. Because depletion
accounts for return flows and captures the share of available wa-
ter that is actually consumed, this study uses a depletion-based
indicator to evaluate water risk. Therefore, the same increase in
consumption can result in different water risk values, depending
on existing consumption and available water where it occurs.
1.1
Related Works and Research Gaps
Data center water–energy assessments have increasingly expanded
the system boundary to include both facility and electricity gen-
eration water use. Early approaches estimated indirect water con-
sumption by applying grid-averaged water consumption factors to
facility electricity use based on regional power mixes [17, 25]. Later
studies incorporated differences in cooling technology, climate, and
regional water availability [9, 10, 21] and, more recently, spatial
and temporal variation in electricity generation and hydrologic
conditions [22, 33]. Across all of these studies, however, the indi-
rect water consumption calculation retains the same fundamental
limitation: it uses the water consumption intensity of an averaged
generation mix rather than identifying the generators whose output
actually changes in response to that demand.
This limitation persists even at higher temporal resolutions. Ex-
isting assessments assign added demand the water consumption
intensity of generation already occurring in the region and period
analyzed [21, 22], assuming generators increase their output in
proportion to the observed mix. This assumption simplifies the true
grid response. These approaches can estimate the water consump-
tion when the generation mix is fairly uniform (e.g., all natural gas,
or all hydro), a limiting assumption for most real-world systems
[13].
This limitation is even more pronounced for spatial impacts. Ag-
gregating generator water consumption into regional electricity
intensities does not preserve the locations of responding genera-
tors, so it cannot assign incremental consumption to the hydrologic
regions where it actually occurs. While direct cooling consumption
falls within the facility’s hydrologic region, the generators respond-
ing to its electricity demand may be located and consume water
in several other regions [17, 21]. Therefore, an assessment based
on the facility location [33] or an aggregated electricity region [22]
may estimate the total indirect consumption volume while misiden-
tifying the regions in which the consumption actually occurs.
1.2
Contributions
Thus, existing approaches cannot resolve which generators respond
to added demand, nor the hydrologic regions in which that re-
sponse’s consumption and depletion occur. To bridge this gap, we
present an integrated water–energy model that connects facility
operations, grid dispatch, and water subbasin conditions to evalu-
ate the water and energy impacts of data center development. We
then use the integrated model to evaluate the impacts of facility
siting, cooling configuration, and computing workload on water
risk, which we define as a depletion-based metric at the subbasin
level. Our model is built using publicly available real-world data,
and used to simulate data center growth in the state of Michigan.
Our case studies show:
• Reducing direct cooling consumption can increase electric-
ity demand and indirect consumption, highlighting why
cooling choices must be evaluated across both the facility
and the specific generators responding to its load.
• Indirect water intensity varies across months as the re-
sponding generators change, revealing temporal differences
that are obscured by applying a fixed regional electricity
water-intensity factor.
• Assigning direct and indirect consumption to their respec-
tive subbasins reveals depletion increases beyond the data
center sites that would be missed by evaluating both com-
ponents using only the facility’s hydrologic boundary.
2
An Integrated Water–Energy Model
The integrated model is composed of three systems:
• DCF System: Data center facility design and opera-
tions. Models data center siting (lat/long coordinates), IT
capacity or total facility capacity, hourly computing load,
cooling configuration, power usage effectiveness (PUE),
and water usage effectiveness (WUE). This system calcu-
lates the Scope 1 water consumption from cooling using
the facility WUE.
• Energy System: Regional power grid operations and
generator dispatch. Models the power grid infrastruc-
ture (substations and transmission lines), hourly regional
electricity demand, and generators. Individual generators’
operating costs and capacity are used in the economic dis-
patch optimization. This system calculates Scope 2 water
consumption from electricity generation using generator
water consumption intensities. The Energy System is cou-
pled with the DCF system through the facility PUE.
• Water System: Consumption and depletion for hydro-
logic regions. Models the hydrologic region boundaries,
and monthly baseline water availability and consumption.
This system calculates the water risk using a depletion-
based metric at the subbasin level. The Water System is
coupled with the other two through the water depletion
from cooling (Scope 1, DCF System) and depletion from
generation (Scope 2, Energy System).
Throughout this paper, indirect consumption refers only to elec-
tricity generation. These pathways do not constitute a complete
life-cycle analysis of the water footprint, as water embodied in fa-
cility construction, server and equipment manufacturing, and other
supply chain activities is considered Scope 3 use and is outside the
model boundary of this study [1].
2.1
DCF System model
Each facility 𝑓∈F is specified by its coordinates, capacity, elec-
tricity load profile, and cooling configuration. The facility capacity
can be defined as either IT demand or total facility load. IT load
includes servers, storage, and networking equipment, while total
facility load includes IT demand as well as cooling, power con-
version, lighting, and other supporting systems [24]. We use PUE
and WUE metrics to determine facility electricity and water use

---

## Page 3

Data Center Cooling Choices Shift Water Impacts Across the Grid
Figure 1: Integrated water–energy model is composed of
three systems: data center facility, energy, and water sys-
tems
for different cooling configurations. These metrics primarily re-
main fixed; however, when modeling cooling configurations with
multiple operating modes, they vary over time with the selected
mode.
2.1.1
IT-load representation. Facility electricity for time interval
𝑡is calculated from the IT load 𝑃IT,𝑓, using the facility’s reported
PUE:
𝐸facility,𝑓= 𝑃IT,𝑓× Δ𝑡× PUE𝑓,
(1)
where 𝑃IT,𝑓is in MW, Δ𝑡is the interval duration in hours, and
𝐸facility,𝑓is in MWh.
2.1.2
Facility-load representation. In this configuration, the total
facility load is
𝐸facility,𝑓= 𝑃facility,𝑓× Δ𝑡
(2)
and the IT load is calculated from the PUE as
𝐸IT,𝑓= 𝐸facility,𝑓
PUE𝑓
.
(3)
2.1.3
Scope 1 Water Consumption. Under both load representa-
tions, the model treats WUE as a consumptive cooling water inten-
sity, denoted as WUE𝑓in L/kWh of IT electricity. Direct consump-
tion is
𝑊direct,𝑓= 𝐸IT,𝑓× WUE𝑓,
(4)
where 𝐸IT,𝑓is in MWh and 𝑊direct,𝑓is in m3.
2.1.4
Industry data: PUE and WUE metrics. The PUE and WUE
metrics are taken from the 2024 Department of Energy report, the
United States Data Center Energy Usage Report [20]. The report
provides simulated ranges of annualized PUE and WUE across data
center space types, IT cooling systems, and heat rejection systems.
These ranges come from thermodynamic-based models evaluated
across surveyed data center operating and climate conditions [20].
It is important to note the distinction between the IT cooling
system (removes heat from the servers) and the heat rejection
system (removes heat from the facility). For example, describing
a system as “liquid cooled” identifies how heat is removed from
the servers but does not establish whether heat is then rejected
from the facility through a cooling tower, fan towers, or other heat
rejection methods. The overall facility cooling configuration in our
model refers to the combination of technologies selected for IT
cooling and facility heat rejection.
Figure 2: Data from the 2024 DOE report on data center en-
ergy usage, showing PUE and WUE ranges by cooling config-
uration and data center size [20](see Figure 4.4)
2.2
Energy System model
The transmission grid is modeled as a graph consisting of electrical
buses (graph nodes) N = {1, ...,𝑛} and transmission lines (graph
edges) L = {1, ...,𝑚}. Transmission line limits are given by 𝐹∈R𝑚.
Generators are represented by a fleet of 𝑘generators with capacity
limits 𝑝∈[𝑃, 𝑃], where 𝑃, 𝑃∈R𝑘
≥0 and linear cost curves of the
form 𝑐𝑝, where 𝑐∈R𝑘
+ is the marginal cost of generation and 𝑝is
the dispatch setpoint. Generators are mapped to buses using matrix
G ∈R𝑛×𝑘, where G𝑖𝑗= 1 if generator 𝑗injects power at bus 𝑖.
Electric load is given by the demand vector 𝑑∈R𝑛
≥0.
2.2.1
Generator data. The generators and their nameplate capac-
ities are taken from the U.S. Energy Information Administration
(EIA) Form 860, which reports power plant and generator data in
the U.S. [28]. Individual generators at the same plant are grouped
by energy technology and represented as a single generator 𝑔in the
grid model with their summed nameplate capacities. Each facility
and generator is assigned to an electrical bus: facility (model input)
and generator coordinates (form EIA-860) are mapped to the closest
bus using the Haversine distance between the two points. The sets
F𝑖and G𝑖denote the facilities and generators assigned to bus 𝑖,
respectively.
2.2.2
Generator availability. Dispatchable generators (e.g., ther-
mal generation and pumped hydro) are assumed to be dispatched
up to their nameplate capacity. Intermittent renewable genera-
tion (e.g., wind and solar) is modeled with hourly availability data,
as a fraction of their nameplate capacity. Wind is modeled using
county-level hourly capacity factors from the Regional Energy De-
ployment System (ReEDS) renewable dataset [19]. Solar is modeled
by matching solar plants to the nearest National Solar Radiation

---

## Page 4

Alston et al.
Database (NSRDB) 4 km resolution location, with hourly avail-
ability approximated from normalized global horizontal irradiance
[18]. All generating technologies are assumed to have no minimum
generation requirements, with the exception of nuclear, which is
assigned a 95% minimum load requirement to represent sustained
operations. Wind and solar generation can be curtailed if available
generation exceeds system load or transmission congestion limits
the deliverability to load sites.
2.2.3
Grid operations and generator dispatch. Generator dispatch
is modeled using the structure of U.S. electricity markets, using a
linearized optimal power flow model. Total system generating cost
is minimized, subject to network constraints (Kirchhoff’s Voltage
and Current Laws, thermal line limits). The optimization output
is the set of generators that are dispatched to supply the system
load, their power setpoints, and total system costs. We use the
open-source PyPSA Python package to model the grid, generators,
and economic dispatch problem, which is solved with the HiGHS
optimization solver [5].
2.2.4
Generator water consumption. The EIA provides monthly
water consumption intensities for generators in the thermoelectric
cooling water dataset, derived from EIA-860 forms [28, 29]. Con-
sumption per unit of generation is expressed in U.S. gal/MWh and
denoted as WCI𝑔,𝑚, and reported for generators with capacities
above 100 MW. To address partial or missing data for generators,
the monthly WCI𝑔,𝑚values are assigned as follows:
(1) Where monthly data is reported for a generator, the generator-
specific values are taken directly from the EIA dataset.
(2) If no information is available for a specific generator in
a given month, but data is available for other generators
of the same technology during that month, it is assigned
the monthly median for its corresponding generation tech-
nology. The monthly median is calculated per technology,
using all available generator data from the EIA dataset.
(3) If no information is available for a specific generator in a
given month and no data is available for other generators of
the same technology during that month, it is assigned the
annual average of available monthly technology medians
for its corresponding generation technology.
(4) If no information is available for any generator of a specific
technology type, the WCI values are manually assigned
from other sources.
The water consumption for a generator 𝑔in month 𝑚is
𝑊generation,𝑔,𝑚= 𝛾× WCI𝑔,𝑚×
∑︁
𝑡∈𝑚
𝑝𝑔,𝑡Δ𝑡,
(5)
where 𝛾converts water volumes from U.S. gallons to m3, Δ𝑡is
the interval duration in hours, and 𝑝𝑔,𝑡is the power dispatch of
the generator 𝑔at time 𝑡in MW. This calculation links the Energy
System to the Water System.
2.3
Water System model
The Water System uses Hydrologic Unit Codes (HUCs) to define
the boundaries of drainage areas. HUC-8 units represent subbasins,
while HUC-12 units represent smaller subwatersheds. Subbasins are
used as the reporting scale because they balance spatial granularity
with regional interpretability. Their scale is coarse enough to avoid
reporting results across hundreds of individual HUC-12 units, while
remaining sufficiently granular to preserve spatial differences in
the HUC-12 data. Note that the proposed model can be resolved at
other hydrologic scales, if sufficient data is available at that spatial
scale. Each facility and generator is assigned to a subbasin: facility
(model input) and generator coordinates (form EIA-860) are mapped
to the containing subbasin polygons. The sets Fℎand Gℎdenote
the facilities and generators assigned to subbasin ℎ, respectively. It
should be noted that this mapping is separate from assignment to
electrical buses – because facilities sharing a bus (subbasin) do not
necessarily share a subbasin (bus).
Monthly baseline conditions come from the U.S. Geological Sur-
vey (USGS) National Water Availability Assessment outputs [31].
The HUC-12 USGS consumption and availability data, where water
quantities are reported as depths in mm/month, are aggregated to
HUC-8 using area-weighted means. Consumption includes water
consumed by public supply, thermoelectric generation, and crop
irrigation, and is cumulative over the local and upstream drainage
area. Availability represents water exiting a HUC-12 after consump-
tive losses, and represents the remaining water available for use
by the facility and generators supplying the additional load. Let
𝐴ℎ,𝑚and 𝐶ℎ,𝑚denote the availability and consumption depths for
month 𝑚at the HUC-8 unit. The gross supply for a subbasin ℎis
𝑆ℎ,𝑚= 𝐴ℎ,𝑚+ 𝐶ℎ,𝑚.
(6)
The resulting supply and consumption depths provide the inputs
for the final depletion-based water risk calculation.
2.4
Water Risk
The integrated water–energy model evaluates the impact of data
center 𝑓by comparing the generation dispatch and water con-
sumption to a baseline without any facility additions. The monthly
change in generation from the facility addition compared to the
baseline is
Δ𝐺𝑔,𝑚=
∑︁
𝑡∈𝑚

𝑝DCF
𝑔,𝑡
−𝑝baseline
𝑔,𝑡

Δ𝑡,
(7)
where Δ𝐺𝑔,𝑚is measured in MWh, and 𝑝DCF
𝑔,𝑡
and 𝑝baseline
𝑔,𝑡
are the
power output of generator𝑔during time interval 𝑡with and without
the data center, respectively. The corresponding change in generator
water consumption is
𝑊indirect,𝑔,𝑚= 𝛾× Δ𝐺𝑔,𝑚× WCI𝑔,𝑚.
(8)
Note that only the change in generator water consumption is added
to the hydrologic baseline because the USGS baseline 𝐶ℎ,𝑚already
includes thermoelectric water use.
Direct and indirect water consumption are aggregated to sub-
basin ℎ, and converted from volume (in 𝑚3) to depth quantities (in
mm) using the subbasin area 𝐴ℎas
𝑊direct,ℎ,𝑚= 1000
𝐴ℎ
∑︁
𝑓∈Fℎ
∑︁
𝑡∈𝑚
𝑊direct,𝑓,𝑡
(9)
𝑊indirect,ℎ,𝑚= 1000
𝐴ℎ
∑︁
𝑔∈Gℎ
𝑊indirect,𝑔,𝑚.
(10)

---

## Page 5

Data Center Cooling Choices Shift Water Impacts Across the Grid
The water depletion for the baseline and facility addition are
𝐷baseline
ℎ,𝑚
= 𝐶ℎ,𝑚
𝑆ℎ,𝑚
,
(11)
𝐷DCF
ℎ,𝑚= 𝐶ℎ,𝑚+𝑊direct,ℎ,𝑚+𝑊indirect,ℎ,𝑚
𝑆ℎ,𝑚
.
(12)
and the absolute change in depletion with the facility addition, in
percentage points (pp), is:
Δ𝐷ℎ,𝑚=

𝐷DCF
ℎ,𝑚−𝐷baseline
ℎ,𝑚

× 100.
(13)
Throughout the calculations, the direct and indirect terms remain
assigned to their respective subbasins, capturing the full spatial
impacts of facility addition beyond the specific site location.
3
Case Study
To demonstrate the framework, the model is implemented using
Michigan-specific data and applied to two scenarios that illustrate
its ability to evaluate different elements of data center development
and its impacts.
3.1
Michigan Model Implementation
3.1.1
Grid data: Michigan’s electricity system is represented using
four regions, each represented as an electrical bus in N: Southeast,
Central, West, and North Michigan. Four transmission corridors
connect Southeast to Central, Southeast to West, Central to West,
and Central to North Michigan. Each corridor has a thermal limit
𝐹= 6, 000 MW, selected heuristically to remain well above expected
interregional power transfers and thereby prevent transmission
congestion from dominating the dispatch results. Individual trans-
mission lines are assigned line reactances of 0.10 Ω and line resis-
tances of 0.01 Ω as heuristic parameters, consistent with values
used in PyPSA’s network examples [16].
3.1.2
Generator data: Michigan has 32.4 GW of installed genera-
tion capacity based on the EIA-860 data [28]. Natural gas accounts
for 44.6% of capacity, followed by coal (19.5%), wind (11.7%), nuclear
(10.8%), hydroelectric generation (7.2%), solar (3.6%), biomass (1.5%),
petroleum (1.3%), and battery storage (less than 0.1%). Based on the
marginal costs assigned to each generating technology, detailed
in Appendix A, the economic dispatch model generally prioritizes
dispatching wind and solar, followed by hydroelectric generation,
nuclear and natural gas, coal, biomass, and petroleum.
The monthly water consumption intensities are assigned based
on the procedure described in Section 2.2.4 (see Appendix A for an-
nualized WCI). The remaining technologies without data reported
in the EIA dataset are assigned the fixed WCI values shown in
Table1. Specific technologies present in Michigan’s generation mix
are treated as follows. Petroleum coke plants operate similarly to
steam coal plants [7, 27], and are assigned the median WCI of steam
coal reported in a study by the National Laboratory of the Rockies
[12]. Hydroelectric generation (conventional and pumped storage)
is assumed to have a WCI of zero. Many studies use high water
consumption values, attributed to evapotranspiration from their
reservoirs [12]. However, WCI is the rate of water consumption per
unit of power produced; the operation of a hydroelectric plant does
not significantly change the evapotranspiration of the reservoir,
Table 1: WCI values for generating technologies not found
in EIA dataset.
Generating technology and source
WCI (gal/MWh)
Batteries 1
0
Conventional hydroelectric 1
0
Hydroelectric pumped storage 1
0
Landfill gas [12]
35
Natural-gas combustion turbine [26]
0
Natural-gas internal-combustion engine [30]
0
Onshore wind [12]
0
Petroleum coke [7, 12, 27]
687
Solar photovoltaic [12]
26
1Values assumed based on technology operations
and water is not otherwise consumed in hydroelectric power gen-
eration. The WCI metric is more accurate in capturing the change
in resource operations due to an addition of load.
3.1.3
Load data: Electric load is constructed from the 2023 hourly
county electricity profiles from the Open Energy Data Initiative’s
demand dataset [15]. Each county is assigned to the nearest bus
based on the Haversine distance from the county’s centroid. The
aggregated hourly electricity demand of all counties mapped to bus
𝑖represents the demand 𝑑𝑖.
3.2
Scenario 1: Evaluating Water–Energy
Tradeoffs from Cooling Configurations
Scenario 1 evaluates three cooling configurations at a hypothetical
data center facility in Oakland County, Southeast Michigan, which
presently has the highest concentration of operating data centers in
the state [2]. The facility has a 200 MW IT load, defined using the
IT-load representation of (1). Under this formulation, the cooling
configuration impacts both direct water consumption (via WUE)
and the facility electricity demand (via PUE), to directly evaluate
water–energy tradeoffs and its spatial impacts.
Three cooling configurations are evaluated: a water-cooled chiller,
an air-cooled chiller, and a hybrid airside economizer paired with
a water-cooled chiller. The water- and air-cooled chiller config-
urations each rely on a single cooling technology and maintain
operations throughout the year. For both configurations, the PUE
and WUE inputs are selected from the upper endpoints of their
respective midsize data center performance ranges [20], represent-
ing worst-case configurations. The hybrid configuration switches
between air-cooled and water-cooled configurations throughout
the year. For the PUE and WUE metrics, the lower endpoints repre-
sent the air-cooled mode because it uses less energy (free/passive
cooling) and less water (non-evaporative), and the upper endpoints
represent the water-cooled mode because it uses more energy (from
pumping and cooling towers) and more water (evaporative).
The daily operating mode is determined based on the daily aver-
age temperature and relative humidity of the site. Data from the
2023 National Solar Radiation Database (NSRDB) are taken from
the grid point nearest the data center site using Haversine distance
[18]. The air-cooled mode (economizer) is selected when the mean
temperature is at or below 27◦C and mean relative humidity is at or

---

## Page 6

Alston et al.
below 70%. If either threshold is exceeded, the water-cooled mode
(chiller) is selected. These thresholds correspond to the maximum
recommended dry-bulb temperature and relative humidity of air
for cooling IT technology in the Federal Energy Management Pro-
gram’s Best Practices Guide for Energy-Efficient Data Center Design
[32].
3.3
Scenario 2: Proposed Michigan Data Center
Build Out
Scenario 2 evaluates three proposed hyperscale data center devel-
opments in Michigan using information collected through Frac-
Tracker’s data center tracking tool [6]. The tracker reports maxi-
mum facility demands of 2,700 MW, 1,400 MW, and 525 MW for the
three selected facilities, resulting in a combined maximum demand
of 4,625 MW. Although the capacity data from real proposed devel-
opments are used, the facility configurations are not known. All
three developments are hyperscale data centers, likely for AI train-
ing workloads. These configurations typically use IT liquid cooling
at the server side, but may use various heat rejection systems. This
scenario assumes all three have IT-liquid cooling with a waterside
economizer and water-cooled chiller, using the respective median
values for PUE and WUE [20].
The facility-load representation of (3) is used, where each facil-
ity’s maximum demand is scaled using the hourly synthetic load
profile [3] and PUE is only used to calculate IT electricity for direct
water consumption:
𝐸facility,𝑓= 𝑃facility,𝑓× 𝐿𝑓,𝑡× Δ𝑡,
(14)
where 𝐿𝑓,𝑡is the fraction of maximum facility demand during in-
terval 𝑡. PUE is then used only to calculate IT electricity using (3),
which determines direct water consumption through (4).
To evaluate the impacts of not only the magnitude of added
load, but also its location, two siting cases are simulated. The base
case places all three facilities at their currently proposed locations
in Southeast Michigan, representing concentrated development.
The alternate case places the same facility loads at hypothetical
locations in West, Southeast, and Central Michigan. These two loca-
tional cases could represent different data center compute: inference
tasks that are latency sensitive may locate closer to users in urban
environments, while AI training tasks that are less latency sensitive
may locate further from users. Since the three facilities have the
same cooling configuration and follow the same load profile, the
total direct water consumption and electric load will be the same
across both cases. However, the location of direct water consump-
tion will vary based on the location of the facility. The indirect
water consumption quantities and locations may also vary, as the
load interacts with both generation and transmission capacity.
Note that this scenario is an illustrative analysis of how signifi-
cant data center additions can impact water and energy systems,
and does not serve as an assessment of the impacts of any specific
project.
4
Results and Discussion
Prior water–energy assessments of data centers have relied on fa-
cility efficiency metrics and average grid water intensity factors
to estimate off-site consumption [10, 11, 17, 20]. Because these
approaches do not identify which generators respond to an incre-
mental load, when that response occurs, or where the resulting
consumption falls relative to existing water conditions, they sup-
press the temporal impacts and misattribute the spatial impacts of
data center loads. Applying our integrated water–energy model to
the Michigan case studies reveals five critical findings that these
simplified approaches cannot capture:
(1) Cooling configuration results in a water–energy tradeoff
(2) Average grid water intensities cannot capture the true indi-
rect water impacts
(3) Data center impacts extend beyond the facility site
(4) Annualized reporting obscures the underlying system con-
ditions
(5) Water consumption magnitude alone cannot determine wa-
ter risk
These findings are discussed next, drawing from the results of
both scenarios. Our findings have direct consequences for how the
water and energy footprint of data center developments should be
assessed, sited, and reported.
4.1
Cooling Configuration Results in a
Water–Energy Tradeoff
Scenario 1 compares three cooling configurations, tracking the
direct and indirect water consumption over a year of operations.
Generally, configurations with lower direct water consumption
(e.g., air-cooled) reduce total modeled water consumption, while
increasing the relative contribution of indirect water use.
Table 2 shows this tradeoff most clearly between the water-
cooled and air-cooled configurations. Moving from the water-cooled
chiller to the air-cooled chiller reduced annual direct water con-
sumption by 97%, from 6.45 to 0.21 million m3, while increasing
facility electricity demand by 32%, from 3.08 to 4.06 TWh. This
additional electricity demand increased indirect water consump-
tion by 32%, from 4.48 to 5.91 million m3. Despite this increase,
total water consumption decreased when moving to the air-cooled
chiller by 44%, from 10.93 to 6.12 million m3. As a result, indirect
water increased from 41% of the total modeled footprint for the
water-cooled chiller to 96.6% for the air-cooled chiller. The selec-
tion of cooling configuration increased the indirect consumption,
shifting the water footprint from the facility site (DCF System) to
the generator sites (Energy System).
The hybrid configuration further illustrates this tradeoff, shifting
between both water-cooled (chiller) and air-cooled (economizer)
modes. Its annual direct water consumption (3.20 million m3) fell
between the two extremes of the water-cooled and air-cooled con-
figurations, but produced the lowest facility electricity demand (2.76
TWh) and indirect water consumption (3.98 million m3) of all three
configurations. Its total water footprint of 7.19 million m3 remained
higher than the air-cooled configuration, but was 34% lower than
the water-cooled configuration. The hybrid configuration captured
the direct water savings from using the air-cooled mode, without
fully absorbing the electricity and indirect water penalties.
This efficiency gain comes with more complex and climate-
dependent operations. Table 3 shows that the hybrid configuration
operated in economizer mode for only 25% of the year, and the

---

## Page 7

Data Center Cooling Choices Shift Water Impacts Across the Grid
Table 2: Annual electricity and water consumption across the modeled cooling and siting cases.
Scenario
Cooling configuration
Facility electricity
(TWh)
Direct water
(million m3)
Indirect water
(million m3)
Total water
(million m3)
Indirect share
(%)
1: Fixed 200 MW IT load
Water-cooled chiller
3.08
6.45
4.48
10.93
41.0
1: Fixed 200 MW IT load
Hybrid airside economizer / water-cooled
chiller
2.76
3.20
3.98
7.19
55.4
1: Fixed 200 MW IT load
Air-cooled chiller
4.06
0.21
5.91
6.12
96.6
2: Base locations (concen-
trated), 4,625 MW build
out
IT liquid cooling: waterside economizer /
water-cooled chiller
36.22
70.71
53.41
124.11
43.0
2: Alternative locations,
4,625 MW build out
IT liquid cooling: waterside economizer /
water-cooled chiller
36.22
70.71
53.42
124.13
43.0
chiller exceeded 80% of days in the months of January and Au-
gust through December. The months with the largest economizer
share were May and June at 68% and 53%, respectively. Figure 3
shows the monthly direct and indirect water consumption for each
cooling configuration in Scenario 1. The water–energy tradeoff
is clearly shown for the hybrid configuration: compare the water
consumption breakdown for May and August. May has among the
lowest direct water consumption, given its high economizer use,
but higher indirect water consumption. August has high direct wa-
ter consumption, attributed to higher use of the chiller mode. The
operating mode did not result in the expected seasonal pattern of
winter-economizer / summer-chiller operations: this is because both
temperature and relative humidity conditions had to be satisfied
to permit economizer operation. The data center located in South-
east Michigan falls under the IECC 5A climate zone (Cool-Humid),
where higher relative humidity restricts how often free-cooling
conditions are met, despite lower temperatures.
Table 3: Monthly operating-mode selection for the hybrid
airside economizer / water-cooled chiller configuration.
Month
Economizer, Air-Cooled (%)
Chiller, Water-cooled (%)
January
10
90
February
25
75
March
19
81
April
33
67
May
68
32
June
53
47
July
32
68
August
16
84
September
10
90
October
13
87
November
17
83
December
3
97
Annual
25
75
4.2
Average Grid Water Intensities Cannot
Capture the True Indirect Water Impacts
Figure 3 shows the monthly direct and indirect water consumption
for each cooling configuration in Scenario 1. For the water-cooled
(evaporative) and air-cooled configurations, the facility’s IT load
is fixed throughout the year, resulting in constant monthly direct
water consumption (via the constant WUE, where minor variations
month-to-month are attributed to the length of the month) and
constant monthly power consumption (via the constant PUE). The
indirect water consumption, however, varies substantially through-
out the year. For example, the indirect water use for the water-
cooled configuration is substantially higher in July than in June.
This monthly variation does not come from variable power de-
mand from the facility, but is driven by variation in (i) generation
availability and (ii) baseline electricity demand. Figure 4 plots the
generation resources dispatched to serve total electric load on the
system (baseline + facility load). Nuclear and hydro resources pro-
vide baseload throughout the year, operating near full capacity.
Wind and solar resources are dispatched when available (inter-
mittent zero-marginal cost generators), and natural gas provides
load-following capabilities.
Figure 3: Monthly direct and indirect water consumption
across cooling configurations
4.3
Data Center Impacts Extend Beyond the
Facility Site
The demonstrated water–energy tradeoff has spatial implications:
while direct water use impacts subbasins at the facility site, the
indirect water use is determined by the generators responding to
the added load. In this way, cooling configuration selection also
changes the spatial impacts of data center development.
In Scenario 1, the location of the facility remains the same, so
changes in direct water consumption impact a single subbasin.
However, when reducing direct water consumption (e.g., switching

---

## Page 8

Alston et al.
Figure 4: Monthly total generation mix across the three cool-
ing configurations in Scenario 1
to air-cooled systems), the corresponding increase in electricity
demand increases the magnitude of indirect water consumption
and depletion in other subbasins. Figure 5 compares the annual
indirect depletion impacts across the three cooling configurations.
The spatial distribution of indirect depletion remained largely con-
sistent across the cooling configurations. This is likely because of
the highly aggregated grid model (only 4 buses and 4 transmission
lines) used to represent the Michigan grid. The low spatial resolu-
tion of the grid infrastructure, despite highly granular data on the
generators and their water intensities, limits the ability to model
variable patterns in grid congestion and the resulting generator
dispatch which would drive spatial variation. However, the magni-
tude of impact within those subbasins varied substantially, with the
air-cooled configuration producing the largest indirect depletion
contributions and the hybrid configuration producing the smallest.
Figure 5: Spatial distribution of indirect water impacts across
cooling configurations
In Scenario 2, the water impact of the proposed data center build
out is distributed spatially throughout the state. Figure 6 shows the
annual depletion at the subbasins with the largest absolute increase
in depletion, denoted by their HUC-8 IDs. The baseline (grey), di-
rect (blue), and indirect (yellow) depletion are tracked, showing the
magnitude of impact from the data center. Under the concentrated
siting case (base case), the three facilities were assigned to two
subbasins in Southeast Michigan, producing subbasin depletion
increases of 6.74% and 2.58%, respectively. For these two subbasins,
indirect consumption contributed less than 0.03% to the total an-
nual increase. The remaining six subbasins experience increased
depletion from indirect water consumption. Of these, the top four
subbasins experience increases in annual depletion ranging from
0.81% to 1.5%, and are located throughout the state, in Southwest,
Southeast, North and Central Michigan. While the largest impacts
remain concentrated around the proposed facilities, direct water
consumption contributes 57% of the water footprint (see Table 2),
while the remaining 43% of water consumption is driven by the En-
ergy System and distributed across generator subbasins elsewhere
in the state. Methodologies such as those proposed by [33] misat-
tribute this consumption to the facility site. The spatial distribution
of total depletion increase is shown in Figure 7(a) and (b) for the
base siting and relocation, respectively. Under the relocated case,
direct consumption is distributed among three HUC-8 subbasins in
Western, Central, and Southeastern Michigan. Although both cases
have the same direct water consumption, the distribution of the
depletion across different locations reduced the impact of the data
center build out: the largest total depletion change in any subbasin
decreased to 2.78% (from 6.74%).
Figure 6: Annual depletion components for the eight HUC-
8 subbasins with the largest depletion increases under the
proposed data center siting scenario
4.4
Annualized Reporting Obscures the
Underlying System Conditions
Figure 8 provides more granular tracking of the water consump-
tion from Scenario 2 (base siting). The plot shows monthly deple-
tion components for the three subbasins with the largest annual
depletion increases. Depletion in each of these subbasins varies
substantially month to month, driven by water availability and its
interactions with the following factors: (i) baseline depletion varies
with existing consumption; (ii) direct consumption varies with the
load profile; and (iii) indirect consumption varies with generation
availability and baseline electricity demand (see Section 4.2).
Overall, depletion percentage is highest during the summer
months due to lower water availability. The two subbasins whose
annual increase is dominated by direct consumption (top two plots)
show elevated depletion for most of the year, consistent with contin-
uous facility water use. The third subbasin, whose annual increase
is entirely from indirect consumption (bottom plot), behaves differ-
ently: depletion rises in the late summer and early fall months of
July, August, and September, when water availability drops, base-
line electric load peaks, and the marginal generators have a higher

---

## Page 9

Data Center Cooling Choices Shift Water Impacts Across the Grid
Figure 7: Scenario 2: Spatial distribution of increase in water
depletion (top: a and b), and total depletion (bottom: c and
d), for the base locations (left) and alternate locations (right).
Facility locations are indicated by yellow dots.
water cost. Annualized totals for this subbasin understate depletion
during these months of high water risk, and overstate depletion in
other months.
Figure 8: Monthly HUC-8 depletion components for the three
most impacted subbasins under the proposed data center
siting scenario
4.5
Water Consumption Magnitude Alone
Cannot Determine Water Risk
Figure 7 compares the increase in depletion from the data center
build out (a and b) to the resulting total depletion once that in-
crease is added to existing baseline conditions (c and d). The same
information is shown for the eight most impacted subbasins in
Figure 6. The comparison of total increase vs. total depletion shows
a mischaracterization of impact when only water consumption
magnitude (or depletion increase) is considered. A large increase in
depletion may not result in a significant impact (e.g., second-ranked
on depletion increase, HUC-8 04100002), while a small increase in
depletion may result in a significant impact (e.g., third-ranked on
depletion increase, but second-ranked on total depletion, HUC-8
04050002). This latter subbasin – which experiences a modest 1.48%
increase in depletion – already has a higher baseline depletion of
4.4% compared to other subbasins. Further, this increase in deple-
tion occurred entirely from indirect consumption: the facility is not
located near this subbasin, and the consumption is entirely from
the response of the electricity system to the added load.
5
Implications for Sustainable Data Center
Development
The results demonstrate that data center water impacts arise from
interactions between cooling configuration, electricity demand, grid
dispatch, and existing hydrologic conditions. Cooling configura-
tion determines direct consumption and facility electricity demand;
grid dispatch determines the magnitude and location of indirect
consumption; and existing subbasin conditions determine how that
consumption translates to water depletion and risk. An assessment
that does not capture all three systems therefore obscures both the
magnitude and location of a data center’s water footprint.
5.1
Recommendations for Industry and Policy
Grounded in engineering modeling and real-world data, the case
study results translate into specific recommendations for industry,
grid planning, and reporting practice:
1. Cooling configuration results in a water–energy tradeoff: Be-
cause PUE and WUE assumptions govern the magnitude of water–
energy tradeoffs and their seasonal shifts, any impact assessment
that assumes annualized fixed values may misrepresent a facility’s
water and energy demands, and its seasonal variation. In Scenario
1, the air-cooled chiller reduced total water consumption, but its
greater electricity demand increased indirect consumption enough
to offset part of that saving; the size of the offset depends on the
generators supplying the additional electricity, so the same cooling
configuration can produce different water outcomes in a differ-
ent grid region. The range of PUE and WUE values per cooling
configuration [20], and the potential for climate-dependent opera-
tion, further highlights the limitations of generalized facility-level
and cooling configuration-type metrics. Without better industry-
reported data on specific cooling technologies and their operations,
water—energy assessments will continue to substitute broad per-
formance ranges for real facility behavior. This gap becomes more
consequential as hybrid and liquid-cooled systems become more
prevalent for AI training infrastructure.

---

## Page 10

Alston et al.
2. Average grid water intensities cannot capture the true indirect
water impacts: Indirect water intensity varies throughout the year,
with different generators responding to the added load. A regional
or averaged water intensity factor assigns a single water cost to
all loads on the system, obscuring the true marginal water cost of
adding a unit of load. To accurately capture these impacts, inte-
grated models are needed to resolve which generators respond to
the added demand, and their corresponding water intensities.
3. Data center impacts extend beyond the facility site: Planning
and siting of new developments must consider water conditions
at proposed facility sites and in the hydrologic regions where the
added electricity generation may increase consumption. The reloca-
tion results show that siting can reduce the concentration of direct
depletion impacts without reducing total consumption, while the
distribution of indirect impacts follows the grid response rather
than the facility location. Distributing data center compute is there-
fore not automatically a better outcome, since the affected subbasins
carry different baseline conditions. Evaluating direct and indirect
consumption together, alongside those baseline conditions, is criti-
cal to sustainable data center development.
4. Annualized reporting obscures the underlying system conditions:
Capturing the temporal variability in system conditions requires
data and reporting of both consumption and water availability
at sub-annual resolutions. Neither facility-level nor grid-average
assessments provide sufficient visibility into the spatio-temporal
variations of system conditions to support sustainable data center
development. Reporting and impact assessments should require sub-
annual, subbasin-level depletion metrics rather than annualized,
system-wide totals.
5. Water consumption magnitude alone cannot determine water
risk: Consumption magnitude and the increase in depletion it pro-
duces cannot substitute for water risk. Risk depends on how added
consumption interacts with existing water uses and availability in
a given subbasin – a function of existing infrastructure, competing
consumption, and hydrologic conditions. Reporting frameworks
for data center water impact should track total depletion, not just
consumption volume or its incremental change.
In summary, facility-level analysis and consumption vol-
umes cannot accurately capture data center impacts. Impact
assessments and tracking must move towards integrated
water—energy models that can quantify impacts at a high
spatial and temporal granularity, across interconnected in-
frastructure and natural systems.
5.2
Model Limitations and Future Work
The integrated water–energy model presented is the first to con-
nect facility cooling configuration, grid dispatch, and subbasin-level
water depletion for assessing data center sustainability. The model
is intentionally modular, and each of its three systems can be ex-
tended to capture additional details as better data, higher-resolution
models, and industry practice become available.
DCF System: Facility assumptions introduce additional simplifi-
cation. The DOE PUE and WUE values used represent estimated
ranges rather than the true values of specific facilities. Further,
the operational model was limited in defining operations-varying
PUE and WUE values. For example, the hybrid configuration in
Scenario 1 used fixed outdoor temperature and humidity thresholds.
This significantly simplifies controls that can be found in systems,
including the ability to mix outdoor cold, high humidity air with
return-air to enable higher airside economizer utilization in the
winter. Second, while the facility load profiles used in Scenario 2
are meant to be representative of an AI hyperscale data center, the
load pattern does not reflect different data center uses: AI train-
ing, inference, or general data I/O, can have substantially different
load shapes and utilization patterns. Incorporating representative,
workload-specific load profiles is a topic of future work.
Energy System: The current grid representation aggregates Michi-
gan into four regions, which limits the spatial resolution at which
indirect water consumption can be assigned to individual genera-
tors and limits the ability to evaluate the impact of transmission
congestion. Higher-resolution grid modeling, capable of resolving
congestion at finer spatial granularity and generator-level dispatch
at finer temporal granularity (e.g., sub-hourly dispatch), is the sub-
ject of ongoing work.
Water System: The hydrological regions are modeled at the sub-
basin (HUC-8) level. Aggregating the consumption data from HUC-
12 to larger HUC-8 regions may average out local differences in
water availability and consumption. The resulting depletion esti-
mates indicate regional patterns; more detailed accounting of local
water supply and use is needed to assess the risks to specific water
regions and sources. Second, assigning a facility or generator to a
subbasin using location and distance may misallocate consumption
if the water is actually sourced from a different subbasin. Additional
data mapping water sources to commercial and municipal users is
necessary to accurately capture these local impacts.
General data limitations: Outdated reporting required the anal-
ysis to combine electricity, weather, generator, and hydrologic
datasets from different years, and gaps in reported generator water
use required substitutions that may not reflect individual generator
performance. More complete and consistent data collection across
these sources would directly improve the model’s estimates and
further strengthen their applicability to real-world conditions.
6
Conclusion
Assessing the water–energy impacts of expanding data center in-
frastructure requires accounting for both direct water consumption
at the facility and indirect water consumption from electricity gener-
ation. This study presents an integrated data center–energy–water
model that links facility cooling, grid dispatch, and subbasin de-
pletion. The results show that cooling configuration shifts water
consumption from the facility to electricity generation, that indi-
rect water intensity varies monthly as the responding generators
change, and that facility siting redistributes impacts across the re-
gion. Together, these findings demonstrate that energy and water
impacts cannot be assessed in isolation, and that sustainable data
center development requires integrated water–energy models to
assess impacts and support decision making in siting, design, and
reporting practices.

---

## Page 11

Data Center Cooling Choices Shift Water Impacts Across the Grid
Acknowledgments
This work is supported by the University of Michigan’s Graham
Sustainability Institute Catalyst Grant.
References
[1] Husam Alissa, Teresa Nick, Ashish Raniwala, Alberto Arribas Herranz, Kali
Frost, Ioannis Manousakis, Kari Lio, Brijesh Warrier, Vaidehi Oruganti, T. J.
DiCaprio, Kathryn Oseen-Senda, Bharath Ramakrishnan, Naval Gupta, Ricardo
Bianchini, Jim Kleewein, Christian Belady, Marcus Fontoura, Julie Sinistore,
Mukunth Natarajan, Lauren Johnson, VeeAnder Mealing, Praneet Arshi, and
Madeline Frieze. 2025. Using Life Cycle Assessment to Drive Innovation for
Sustainable Cool Clouds. Nature 641 (2025), 331–338. doi:10.1038/s41586-025-
08832-3
[2] Rahil Banthia. 2026. US Data Center Map. Interactive web map. https://dcmap.
us/?c=42.5697%2C-84.5122%2C6.62 Data updated August 2026.
[3] Molly Bertolacini, Shana Ramirez, Megan Ahern, Anna Clark, and Kush Patel.
2026. Beyond the Headlines: An Empirical Analysis of Data Center Grid Utilization,
Cost-of-Service and Revenue Contributions. Technical Report. Energy and Envi-
ronmental Economics, Inc. https://www.ethree.com/wp-content/uploads/2026/
06/E3_Large-Load-Economics_June-2026.pdf Report funded by CloudHQ, LLC.
[4] Kate A. Brauman, Brian D. Richter, Sandra Postel, Marcus Malsy, and Martina
Flörke. 2016. Water Depletion: An Improved Metric for Incorporating Seasonal
and Dry-Year Water Scarcity into Water Risk Assessments. Elementa: Science of
the Anthropocene 4 (2016), 000083. doi:10.12952/journal.elementa.000083
[5] Tom Brown, Jonas Hörsch, and David Schlachtberger. 2018. PyPSA: Python
for Power System Analysis. Journal of Open Research Software 6, 1 (2018), 4.
doi:10.5334/jors.188
[6] FracTracker Alliance. 2026. Open U.S. Data Centers Tracker. Interactive dataset.
https://fractracker.org/data-centers/ Updated regularly.
[7] Yasunori Hirayama, Masashi Hishida, Yoshihisa Yamamoto, Shuji Makiura, Yoshi-
hisa Arakawa, and Akiyasu Okamoto. 2007. Continuous Operation and Mainte-
nance Results of Power Station with Petroleum Coke Firing Boiler. Mitsubishi
Heavy Industries Technical Review 44, 4 (Dec. 2007).
https://www.mhi.com/
technology/review/sites/g/files/jwhtju2326/files/tr/pdf/e444/e444038.pdf
[8] International Energy Agency. 2025. Energy and AI. Technical Report. Interna-
tional Energy Agency, Paris. https://www.iea.org/reports/energy-and-ai
[9] Leila Karimi, Reema Shinh, Colin Laisure-Pool, Michael Green, Leeann Yacuel,
Jamie Ashby, and Kerri L. Hickenbottom. 2025. Energy and Water Dynamics
in Data Center Cooling: Insights from a Modeling Study in Hot-Arid Climates.
Applied Thermal Engineering (2025), 126802. doi:10.1016/j.applthermaleng.2025.
126802
[10] Nuoa Lei, Jun Lu, Zhu Cheng, Zhi Cao, Arman Shehabi, and Eric Masanet. 2023.
Geospatial Assessment of Water Footprints for Hyperscale Data Centers in
the United States. Journal of Physics: Conference Series 2600, 17 (2023), 172003.
doi:10.1088/1742-6596/2600/17/172003
[11] Nuoa Lei, Jun Lu, Arman Shehabi, and Eric Masanet. 2025. The Water Use
of Data Center Workloads: A Review and Assessment of Key Determinants.
Resources, Conservation and Recycling 219 (2025), 108310. doi:10.1016/j.resconrec.
2025.108310
[12] Jordan Macknick, Robin Newmark, Garvin Heath, and K. C. Hallett. 2011. A
Review of Operational Water Consumption and Withdrawal Factors for Electric-
ity Generating Technologies. Technical Report NREL/TP-6A20-50900. National
Renewable Energy Laboratory. doi:10.2172/1009674
[13] Gregory J. Miller, Kevin Novan, and Alan Jenn. 2022. Hourly Accounting of
Carbon Emissions from Electricity Consumption. Environmental Research Letters
17, 4 (April 2022), 044073. doi:10.1088/1748-9326/ac6147
[14] David Mytton. 2021. Data Centre Water Consumption. npj Clean Water 4 (2021),
11. doi:10.1038/s41545-021-00101-w
[15] Kodi Obika, Wesley Cole, and Marie Rivers. 2025. Hourly Electricity Demand
Profiles for Each County in the Contiguous United States. Open Energy Data
Initiative, dataset 8562. doi:10.25984/3366592 First published November 5, 2025;
2016–2023 estimated hourly demand.
[16] PyPSA Developers. [n. d.]. Newton-Raphson Power Flow: Minimal Three-Node
Network. https://docs.pypsa.org/v1.0.4/examples/minimal-example-pf/
[17] Bora Ristic, Kaveh Madani, and Zen Makuch. 2015. The Water Footprint of Data
Centers. Sustainability 7, 8 (2015), 11260–11284. doi:10.3390/su70811260
[18] Manajit Sengupta, Yu Xie, Anthony Lopez, Aron Habte, Galen Maclaurin, and
James Shelby. 2018. The National Solar Radiation Data Base (NSRDB). Renewable
and Sustainable Energy Reviews 89 (2018), 51–60. doi:10.1016/j.rser.2018.03.003
[19] Brian Sergi, Wesley Cole, Anthony Lopez, Travis Williams, Claire Nguyen, Matt
Mowers, Marie Rivers, and Pavlo Pinchuk. 2025. 2024 County-Level Hourly
Renewable Capacity Factor Dataset for the ReEDS Model. Open Energy Data
Initiative, dataset 8379. https://data.openei.org/submissions/8379
[20] Arman Shehabi, Sarah Josephine Smith, Alex Hubbard, Alexander Newkirk,
Nuoa Lei, Md AbuBakar Siddik, Billie Holecek, Jonathan G. Koomey, Eric R.
Masanet, and Dale A. Sartor. 2024. 2024 United States Data Center Energy Usage
Report. Technical Report LBNL-2001637. Lawrence Berkeley National Laboratory.
doi:10.71468/P1WC7Q
[21] Md Abu Bakar Siddik, Arman Shehabi, and Landon Marston. 2021. The Environ-
mental Footprint of Data Centers in the United States. Environmental Research
Letters 16, 6 (2021), 064017. doi:10.1088/1748-9326/abfba1
[22] Md Abu Bakar Siddik, Arman Shehabi, Prakash Rao, and Landon T. Marston. 2024.
Spatially and Temporally Detailed Water and Carbon Footprints of U.S. Electricity
Generation and Use. Water Resources Research 60, 12 (2024), e2024WR038350.
doi:10.1029/2024WR038350
[23] Sarah J. Smith, Alex Hubbard, Alex Newkirk, Mohan Ganeshalingam, Billie
Holecek, Dale Sartor, Michael Mills, and Arman Shehabi. 2026. United States
Data Center Energy Usage Report: 2025 Update. Technical Report LBNL-2001758.
Lawrence Berkeley National Laboratory. doi:10.71468/P1RP4F
[24] Kaiyu Sun, Na Luo, Xuan Luo, and Tianzhen Hong. 2021. Prototype Energy
Models for Data Centers. Energy and Buildings 231 (2021), 110603. doi:10.1016/j.
enbuild.2020.110603
[25] The Green Grid. 2011. Water Usage Effectiveness (WUE): A Green Grid Data
Center Sustainability Metric. Technical Report White Paper 35. The Green Grid.
https://www.thegreengrid.org/system/files/store/WUE_v1.pdf
[26] U.S. Department of Energy. 2002. Environmental Assessment for Installation and
Operation of Combustion Turbine Generators at Los Alamos National Laboratory,
Los Alamos, New Mexico. Technical Report DOE/EA-1430. U.S. Department of
Energy. https://www.energy.gov/nepa/articles/ea-1430-final-environmental-
assessment
[27] U.S. Energy Information Administration. 2020. More than 100 Coal-Fired Plants
Have Been Replaced or Converted to Natural Gas since 2011. https://www.eia.
gov/todayinenergy/detail.php?id=44636
[28] U.S. Energy Information Administration. 2024. Form EIA-860 Detailed Data:
2024 Reporting Year. U.S. Energy Information Administration, data release.
https://www.eia.gov/electricity/data/eia860/
[29] U.S. Energy Information Administration. 2024. Thermoelectric Cooling Water
Data: 2024 Reporting Year. U.S. Energy Information Administration, data release.
https://www.eia.gov/electricity/data/water/
[30] U.S. Environmental Protection Agency. 2017.
Catalog of CHP Technologies.
Technical Report. U.S. Environmental Protection Agency, Combined Heat and
Power Partnership. https://www.epa.gov/sites/default/files/2015-07/documents/
catalog_of_chp_technologies.pdf
[31] U.S. Geological Survey. 2025.
National Water Availability Assess-
ment Data Companion: National Water Availability Assessment Out-
puts (CONUS 2025).
U.S. Geological Survey, modeled data outputs.
https://water.usgs.gov/nwaa-data/data-catalog/sector/integrated-water-
availability/model/iwa-assessment-outputs-conus-2025/
Monthly HUC12
model outputs for 2010–2020; analysis uses calendar year 2019.
[32] Otto Van Geet and David Sickinger. 2024. Best Practices Guide for Energy-Efficient
Data Center Design. Technical Report DOE/GO-102024-6283. National Renewable
Energy Laboratory. https://www.energy.gov/sites/default/files/2024-07/best-
practice-guide-data-center-design.pdf Revised July 2024; prepared for the U.S.
Department of Energy Federal Energy Management Program.
[33] Yanran Wu, Inez Hua, and Yi Ding. 2025. Not All Water Consumption Is Equal:
A Water Stress Weighted Metric for Sustainable Computing. ACM SIGEnergy
Energy Informatics Review 5, 2 (2025), 84–90. doi:10.1145/3757892.3757904

---

## Page 12

Alston et al.
A
Generator and Water Consumption Intensity
Data
Table A.1 reports the modeled installed generating capacity derived
from the 2024 EIA-860 plant and generator datasets [28].
Table A.1: Modeled Michigan installed generating capacity.
Carrier
Capacity (MW)
Plants
Share (%)
Natural gas
14,445.7
58
44.6
Coal
6,306.9
5
19.5
Wind
3,777.3
34
11.7
Nuclear
3,502.3
2
10.8
Hydroelectric
2,327.1
52
7.2
Solar
1,159.1
61
3.6
Biomass
479.8
31
1.5
Petroleum
410.2
21
1.3
Battery storage
1.4
2
0.0
Total
32,409.8
266
100.0
Table A.2 summarizes the marginal cost assumptions used in the
economic dispatch model for each grouped generating technology.
Table A.2: Carrier-level marginal-cost assumptions used for
dispatch.
Carrier
Cost ($/MWh)
Wind and solar
0
Hydroelectric
15
Nuclear
23
Natural gas
23
Coal
41
Biomass
45
Other generation
60
Petroleum
90
For reference, Table A.3 summarizes the annual water consump-
tion intensity values across the grouped generating technologies
represented in the model. Each value is the arithmetic mean of the
annual generator WCI values within that technology group.
Table A.3: Mean annual WCI by grouped generating technol-
ogy.
Grouped generating technology
WCI (gal/MWh)
Petroleum
831.65
Nuclear
671.33
Coal
523.95
Biomass
336.00
Natural gas
193.49
Solar
26.00
Hydroelectric
0.00
Battery storage
0.00
Wind
0.00