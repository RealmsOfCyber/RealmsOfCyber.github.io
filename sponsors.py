sponsors = {
    "Platinum": [
        {
            "name": "Queensland Government",
            "url": "https://www.qld.gov.au/",
            "logo": "qldgov.png"
        }
    ],
    "Gold": [
        {
            "name": "Cultural Cyber Security",
            "url": "https://www.culturalcybersecurity.com",
            "logo": "ccs.jpg"
        },
    #     {
    #         "name": "Tayko Group",
    #         "url": "https://tayko.io",
    #         "logo": "tayko.png"
    #     },
    #     {
    #         "name": "EAGLEGATE Lawyers",
    #         "url": "https://www.eaglegate.com.au/",
    #         "logo": "eaglegate.jpeg"
    #     }
    ],
    "Silver": [
        {
            "name": "Tarian Cyber",
            "url": "https://tarian.com.au/",
            "logo": "tarian.png"
        },
        {
            "name": "Siege Cyber",
            "url": "https://www.siegecyber.com.au",
            "logo": "siegecyber.png"
        },
        {
            "name": "Silent Grid",
            "url": "https://www.silentgrid.com/",
            "logo": "silentgrid.png"
        },
    #     {
    #         "name": "Sekuro",
    #         "url": "https://sekuro.io",
    #         "logo": "sekuro.png"
    #     },
    #     {
    #         "name": "Redwood Consulting",
    #         "url": "https://www.redwoodsecurity.com.au/",
    #         "logo": "redwood.png"
    #     },
    #     {
    #         "name": "Adrenalan",
    #         "url": "https://www.adrenalan.com/",
    #         "logo": "adrenalan.png"
    #     },
    #     {
    #         "name": "Infotrust",
    #         "url": "https://www.infotrust.com.au/",
    #         "logo": "infotrust.png"
    #     }
    ],
    "Bronze": [
        {
            "name": "Decipher Bureau",
            "url": "https://www.decipherbureau.com/",
            "logo": "decipher.png"
        },
        {
            "name": "Flame Tree Cyber",
            "url": "https://www.flametreecyber.com.au/",
            "logo": "flame_tree_cyber.png"
        },
    #     {
    #         "name": "AusCERT",
    #         "url": "https://auscert.org.au/",
    #         "logo": "auscert.svg"
    #     },
    #     {
    #         "name": "Payatu",
    #         "url": "https://payatu.com/",
    #         "logo": "payatu.png"
    #     },
    #     {
    #         "name": "Jepsec",
    #         "url": "https://jepsec.com.au/",
    #         "logo": "jepsec.webp"
    #     },
    #     {
    #         "name": "Baidam Solutions",
    #         "url": "https://www.baidam.com.au/",
    #         "logo": "baidam.svg"
    #     },
    #     {
    #         "name": "CyberSec People",
    #         "url": "https://www.cybersecpeople.com/",
    #         "logo": "cybersec_people.svg"
    #     },
    #     {
    #         "name": "elttam",
    #         "url": "https://www.elttam.com/",
    #         "logo": "elttam.png"
    #     },
    #     {
    #         "name": "Radiant Security",
    #         "url": "https://radiant.security",
    #         "logo": "radiant.png"
    #     },
    #     {
    #         "name": "ZEV Integrations",
    #         "url": "https://zevint.au/",
    #         "logo": "zev.png"
    #     },
    #     {
    #         "name": "Griffith University",
    #         "url": "https://www.griffith.edu.au/",
    #         "logo": "griffith_university.png"
    #     },
    #     {
    #         "name": "Galah Cyber",
    #         "url": "https://www.galahcyber.com.au/",
    #         "logo": "galah.png"
    #     },
    #     {
    #         "name": "Netskope",
    #         "url": "https://www.netskope.com/",
    #         "logo": "netskope.png"
    #     },
    #     {
    #         "name": "Tom Shaw",
    #         "url": "https://tomshaw.com/",
    #         "logo": "tomshaw.png"
    #     },
    #     {
    #         "name": "Jypra Group",
    #         "url": "https://jypragroup.com.au/",
    #         "logo": "jypra_group.png"
    #     },
    #     {
    #         "name": "Volkis",
    #         "url": "https://www.volkis.com.au/",
    #         "logo": "volkis.png"
    #     },
    #     {
    #         "name": "SecAlerts",
    #         "url": "https://secalerts.co/",
    #         "logo": "secalerts.png"
    #     },
    #     {
    #         "name": "CYBERON",
    #         "url": "https://cyberon.com.au",
    #         "logo": "cyberon.png"
    #     },
    #     {
    #         "name": "Hudson",
    #         "url": "https://au.hudson.com/",
    #         "logo": "hudson.png"
    #     },
    #     {
    #         "name": "IBM",
    #         "url": "https://www.ibm.com/services/security",
    #         "logo": "ibm.png"
    #     },
    #     {
    #         "name": "Acumenis",
    #         "url": "https://www.acumenis.com.au/",
    #         "logo": "acumenis.png"
    #     },
    #     {
    #         "name": "Orca Cyber Solutions",
    #         "url": "https://www.orcacyber.com.au/",
    #         "logo": "orca.png"
    #     }
    ]
}
for level in sponsors.keys():
    sponsors_level = sponsors[level]
    sponsors_build = []
    for sponsor in sponsors_level:
        if not sponsor.get("height"):
            if level == "Platinum":
                sponsor['height'] = 110
            elif level == "Gold":
                sponsor['height'] = 90
            elif level == "Silver":
                sponsor['height'] = 70
            else:
                sponsor['height'] = 60
        if not sponsor.get("width"):
            if level == "Platinum":
                sponsor['width'] = 320
            elif level == "Gold":
                sponsor['width'] = 260
            elif level == "Silver":
                sponsor['width'] = 220
            else:
                sponsor['width'] = 180
        sponsors_build += [sponsor]
    sponsors[level] = sponsors_build