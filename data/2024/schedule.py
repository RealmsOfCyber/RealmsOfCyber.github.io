# Schedule data format:
# schedules = {
#     "schedule_1": {
#         "name": "schedule",  # Internal identifier (used for HTML id)
#         "title": "Schedule",  # Display title shown in the view
#         "items": [
#             # For talks with speakers:
#             {
#                 "time": "9:00 - 9:30",
#                 "title": "Talk Title",
#                 "realm": "Space",  # One of: Space, Cognitive, Land, Sea, Air, Biological, Multi
#                 "speaker": {
#                     "name": "Speaker Name",
#                     "image": "speaker_image.jpg"
#                 },
#                 "desc": "Talk description"
#             },
#             # For non-talk items (breaks, Q&A, etc.):
#             {
#                 "time": "10:00 - 10:30",
#                 "title": "Morning Tea Break"
#             },
#             ...
#         ]
#     },
#     "schedule_2": {
#         "name": "ot-cybersecurity-stream",
#         "title": "OT Cybersecurity Stream",
#         "items": [...]
#     }
# }
# Realm icons are automatically added based on realm name.
# Speaker images should be in: site/assets/images/{year}/speakers/
schedules = {
    "schedule_1": {
        "name": "schedule",
        "title": "Schedule",
        "items": [
            {
                "time": "8:00 - 9:00",
                "title": "Registration"
            },
            {
                "time": "9:00 - 9:15",
                "title": "Opening Words"
            },
            {
                "time": "9:15 - 9:35",
                "title": "Secrets to Success in Dynamic Startups: Insights from SpaceX and Beyond",
                "realm": "Space",
                "speaker": {
                    "name": "Nicholas Lindsay",
                    "image": "nicholas_lindsay.jpg"
                },
                "desc": "Join us for an insightful presentation by an aerospace engineer with experience in the US Navy and leading startup companies including SpaceX, Gilmour Space Technologies, and Hypersonix. Drawing on over a decade of experience in fast-paced start-ups, this talk will uncover the secrets to success in the dynamic startup environment and how these lessons can contribute to a safer and more secure digital world.."
            },
            {
                "time": "9:35 - 9:50",
                "title": "Enhancing Embedded Security Assessments",
                "realm": "Multi",
                "speaker": {
                    "name": "Kylie McDevitt",
                    "image": "kylie_mcdevitt.jpg"
                },
                "desc": "IoT devices have become pervasive in the way we live and interact with the world. In order to provide security assessments on the wide variety of devices on the market, InfoSect has had to expand their capabilities. This talk will walk through InfoSect's improved process for performing security assessment on embedded devices."
            },
            {
                "time": "9:50 - 10:05",
                "title": "Unlocking the Future: SDW Swiff Army Tools in Automotive Security",
                "realm": "Land",
                "speaker": {
                    "name": "David Middleton",
                    "image": "david_middleton.jpeg"
                },
                "desc": "This presentation delves into the change from physical penetration mechanisms to modern Software-Defined Radio (SDR) devices in the context of automotive security. As vehicles increasingly incorporate advanced technologies and connected features, the attack surface has expanded dramatically, exposing non-contact vulnerabilities that were once not realistic. The session will explore how SDR devices can be exploited to intercept keyless entry signals, manipulate vehicle systems, and hijack vehicle control networks"
            },
            {
                "time": "10:05 - 10:20",
                "title": "Securing the Seas: From Pirate Threats to Cyber Attacks",
                "realm": "Sea",
                "speaker": {
                    "name": "Bradley Butler",
                    "image": "bradley_butler.jpg"
                },
                "desc": "Join Brad for a session on the evolution of maritime security threats, where you will journey from traditional piracy to the emerging challenge of cyber attacks. Discover how the landscape of maritime security has transformed over the years and the innovative strategies being employed to combat these threats. Featuring an in-depth case study on modern-day piracy defense and a detailed look into an onboard cyber assessment for a ship."
            },
            {
                "time": "10:20 - 10:35",
                "title": "Minding the Gap Between Pentest Tooling and Railway Systems",
                "realm": "Land",
                "speaker": {
                    "name": "Anthony Caulfield",
                    "image": "anthony_caulfield.jpg"
                },
                "desc": "Wireless networks used in the railway environment can make use of common standards and commodity hardware, others are customised and can seem invisible to our usual attack techniques. This presentation will discuss one such customisation, the challenges with using our standard pentest tooling, and how to better uncover and pentest these networks."
            },
            {
                "time": "10:35 - 10:45",
                "title": "Group 1 Q&A Session"
            },
            {
                "time": "10:45 - 11:30",
                "title": "Morning Tea Break"
            },
            {
                "time": "11:30 - 11:45",
                "title": "Refactoring Security of the Internet to Achieve Quantum Safety",
                "realm": "Multi",
                "speaker": {
                    "name": "Chris Hockings",
                    "image": "chris_hockings.jpeg"
                },
                "desc": "Quantum computers are expected to revolutionise compute, not replacing contemporary systems, but augmenting for specific industry use cases where big data analytics with heavy factorial computation is required. Quantum computers are known to be capable of breaking traditional encryption, through Shor's algorithm. Moving to a Quantum safe world will require new capability, and a focus on quantum risk focus on data security. In this session, Chris will talk through what this means for the world, and the timeframe that action will be required for every organisation, government and software/hardware suppliers."
            },
            {
                "time": "11:45 - 12:00",
                "title": "Information Warfare",
                "realm": "Cognitive",
                "speaker": {
                    "name": "James Carlopio",
                    "image": "james_carlopio.jpg"
                },
                "desc": "Dr. Carlopio will discuss information warfare, from both the Nation-State sponsored and cybercrime perspectives, looking at recent examples, what we can expect in the not-too-distant future, and what we can do about it."
            },
            {
                "time": "12:00 - 12:15",
                "title": "OT Systems Are Systems Too: Response Considerations to an Attack on an Industrial System",
                "realm": "Multi",
                "speaker": {
                    "name": "Alex Tilley",
                    "image": "alex_tilley.jpg"
                },
                "desc": "Preparedness and response considerations to an attack (ransomware or more subtle) on crucial OT/industrial systems. Many considerations are identical to standard IT systems but some unique aspects and stakeholders need to be considered. A session designed to spur internal discussion as organisations plan."
            },
            {
                "time": "12:25 - 12:30",
                "title": "Group 2 Q&A Session"
            },
            {
                "time": "12:30 - 1:40",
                "title": "Lunch Break"
            },
            {
                "time": "1:40 - 1:55",
                "title": "Cyberwar",
                "realm": "Multi",
                "speaker": {
                    "name": "Edward Farrell",
                    "image": "edward_farrell.jpeg"
                },
                "desc": "How does conflict and cyber effects play out into the real world Whilst a lot of theory, speculation and \"Cyber is good children are our future\" conceptual thinking plays out, there are some realities to appreciate if contention or outright conflict takes place. I wanted to work through recent occurrences in Ukraine, the influence conflict plays as well as technical appreciation for prospective scenarios that may exist in Australia and the Asia Pacific."
            },
            {
                "time": "1:55 - 2:10",
                "title": "The Future of Vehicular Autonomy and Its Interplay with Critical Infrastructure Cybersecurity",
                "realm": "Land",
                "speaker": {
                    "name": "Daniel Castillo",
                    "image": "daniel_castillo.jpg"
                },
                "desc": "Critical Infrastructure is often considered the backbone for essential services required for everyday life including energy, food, water, transport, communications, health, commodity vehicular automation, new security concerns emerge not only for auto manufacturers but also asset owners operating Critical Infrastructure. In a highly connected future, use-cases for integration (or interfacing) between vehicular systems and critical infrastructure introduce a range of new threat vectors for attackers to exploit. As a result, there is an increasing need for standardisation which demands these critical infrastructure space, a look into the history of connectivity in operational technology environments (and its security implications), and the relevance of critical infrastructure to autonomous vehicular systems in relevant sectors. Attendees will walk away with a deeper understanding of the interplay between critical infrastructure assets, vehicular systems, associated security implications, and proposed concepts for addressing security standardisation (and resilience) in these areas."
            },
            {
                "time": "2:10 - 2:25",
                "title": "Cybers Beyond the Earth",
                "realm": "Space",
                "speaker": {
                    "name": "Chathura Abeydeera",
                    "image": "chathura_abeydeera.jpg"
                },
                "desc": "As our reliance on space-based technologies expands, so does the urgency to protect these assets from evolving cyber threats. This will explore key challenges such as securing satellite communication networks, mitigating risks to orbital platforms, and defending against sophisticated cyber attacks targeting space infrastructure. In this climate, innovative approaches and strategies essential for building resilient and secure space systems. Get ready to uncover the complexities and advancements in safeguarding our national interests beyond Earth's atmosphere."
            },
            {
                "time": "2:25 - 2:40",
                "title": "Cross-Domain Security in Converged IT/OT",
                "realm": "Multi",
                "speaker": {
                    "name": "Travis Quinn",
                    "image": "travis_quinn.jpg"
                },
                "desc": "The industry is experiencing a shift away from isolated operational technology (OT) systems towards a model where those systems are integrated into the enterprise information technology (IT) environment. While this model has many advantages, bridging IT and OT domains also invites new threats that challenge our existing security methods. Specifically, the convergence of IT and OT challenges how we perform and secure cross-domain communications. Many organisations lack the knowledge, expertise and technical rigour required to do cross-domain security effectively. This presentation explores the problem of cross-domain security in onverged IT/OT by first defining the problem, then describing the requirements and components of a cross-domain solution (CDS) for converged IT/OT, and finally, providing a CDS reference architecture for converged IT/OT based on best practice from industry and government."
            },
            {
                "time": "2:40 - 2:50",
                "title": "Group 3 Q&A Session"
            },
            {
                "time": "2:50 - 3:45",
                "title": "Afternoon Tea Break"
            },
            {
                "time": "3:45 - 4:00",
                "title": "Safeguarding Operational Technology Against Cyber Risks",
                "realm": "Multi",
                "speaker": {
                    "name": "Sadeed Tirmizey",
                    "image": "sadeed_tirmizey.jpg"
                },
                "desc": "More details coming soon..."
            },
            {
                "time": "4:00 - 4:15",
                "title": "Guardians of the Health Tech Galaxy: Cybersecurity Edition",
                "realm": "Biological",
                "speaker": {
                    "name": "Sanja Marais",
                    "image": "sanja_marais.jpg"
                },
                "desc": "Join me for a thrilling adventure as we explore \"Guardians of the Health Tech Galaxy: Cybersecurity Edition.\" Diving into what happens when medical devices go rogue, how transcriptions can get lost in translation, why health data is the new oil, and savvy strategies to outsmart cyber villains. Let's gaze into the future with AI, blockchain, and quantum computing, and see how these innovations are shaping the next frontier of cybersecurity in healthcare."
            },
            {
                "time": "4:15 - 4:30",
                "title": "CAN Bus Hacking",
                "realm": "Land",
                "speaker": {
                    "name": "Sam kelly",
                    "image": "sam_kelly.jpg"
                },
                "desc": "Despite the Controller Area Network (CAN) protocol being around since the 1980s, it remains a daunting challenge for backyard mechanics and cybersecurity red teamers alike. In this presentation, Sam will guide you through the process of procuring and reverse engineering unknown data on a vehicle's CAN Bus. Learn how attackers might exploit this information to bypass security controls and how entrepreneurs could develop vehicle-specific products for the market. Plus, for the sheer fun of it, discover how Sam made his car run DOOM."
            },
            {
                "time": "4:30 - 4:45",
                "title": "Cerberus MI Kinetic Effects with AI Targeting",
                "realm": "Air",
                "speaker": {
                    "name": "Michael Creagh",
                    "image": "michael_creagh.jpg"
                },
                "desc": "The Cerberus MI UAS is a man-packable, lethal 22 kg sUAS. Armed with a 40mm Low velocity grenade launcher, 12 Ga  shotgun, 5.7 x 28mm Submachine gun or M72 LAW, it is intended to be used at the Company and platoon level to provide target recognition (by A thena AI) which enables \"slew-to-cue\" semi-automated  targeting. This has been demonstrated in live fire exercises to the USMC, ADF and US Army. The Cerberus MI is a modular payload to enable integration of a variety of kinetic and address the current state of the  Cerberus and its targeting system (including limitations) and  cyber resilience strategies employed."
            },
            {
                "time": "4:45 - 4:55",
                "title": "Group 4 Q&A Session"
            },
        ]
    },
    "schedule_2": {
        "name": "ot-cybersecurity-stream",
        "title": "OT Cybersecurity Stream",
        "items": []
    },
}
