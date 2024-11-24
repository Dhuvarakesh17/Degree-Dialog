# college_info.py

colleges = {
    'IIT Madras': {
        'name': 'Indian Institute of Technology Madras',
        'description': 'Autonomous public technical and research university located in Chennai, Tamil Nadu.',
        'location': 'Chennai, Tamil Nadu',
        'website': 'https://www.iitm.ac.in/'
    },
    'IIT Delhi': {
        'name': 'Indian Institute of Technology Delhi',
        'description': 'Autonomous public technical and research university located in New Delhi.',
        'location': 'New Delhi',
        'website': 'https://www.iitd.ac.in/'
    },
    'IIT Bombay': {
        'name': 'Indian Institute of Technology Bombay',
        'description': 'Autonomous public technical and research university located in Mumbai, Maharashtra.',
        'location': 'Mumbai, Maharashtra',
        'website': 'https://www.iitb.ac.in/'
    },
    'IIT Kanpur': {
        'name': 'Indian Institute of Technology Kanpur',
        'description': 'Autonomous public technical and research university located in Kanpur, Uttar Pradesh.',
        'location': 'Kanpur, Uttar Pradesh',
        'website': 'https://www.iitk.ac.in/'
    },
    'IIT Kharagpur': {
        'name': 'Indian Institute of Technology Kharagpur',
        'description': 'Autonomous public technical and research university located in Kharagpur, West Bengal.',
        'location': 'Kharagpur, West Bengal',
        'website': 'https://www.iitkgp.ac.in/'
    },
    'Anna University': {
        'name': 'Anna University',
        'description': 'A public technical university located in Chennai, Tamil Nadu.',
        'location': 'Chennai, Tamil Nadu',
        'website': 'https://www.annauniv.edu/'
    },
    'NIT Trichy': {
        'name': 'National Institute of Technology, Tiruchirappalli',
        'description': 'Autonomous public technical and research university located in Tiruchirappalli, Tamil Nadu.',
        'location': 'Tiruchirappalli, Tamil Nadu',
        'website': 'https://www.nittrichy.ac.in/'
    },
    'VIT Vellore': {
        'name': 'Vellore Institute of Technology',
        'description': 'Private deemed university located in Vellore, Tamil Nadu.',
        'location': 'Vellore, Tamil Nadu',
        'website': 'https://www.vit.ac.in/'
    },
    'SSN College of Engineering': {
        'name': 'Sri Sivasubramaniya Nadar College of Engineering',
        'description': 'Private engineering college located in Chennai, Tamil Nadu.',
        'location': 'Chennai, Tamil Nadu',
        'website': 'https://www.ssn.edu.in/'
    },
    'Sathyabama University': {
        'name': 'Sathyabama University',
        'description': 'Private deemed university located in Chennai, Tamil Nadu.',
        'location': 'Chennai, Tamil Nadu',
        'website': 'https://www.sathyabama.ac.in/'
    },
    'PSG College of Technology': {
        'name': 'PSG College of Technology',
        'description': 'Private engineering college located in Coimbatore, Tamil Nadu.',
        'location': 'Coimbatore, Tamil Nadu',
        'website': 'https://www.psgtech.edu.in/'
    },
    'Government College of Technology, Coimbatore': {
        'name': 'Government College of Technology, Coimbatore',
        'description': 'Government engineering college located in Coimbatore, Tamil Nadu.',
        'location': 'Coimbatore, Tamil Nadu',
        'website': 'https://www.gctcoimbatore.ac.in/'
    },
    'Thiagarajar College of Engineering': {
        'name': 'Thiagarajar College of Engineering',
        'description': 'Private engineering college located in Madurai, Tamil Nadu.',
        'location': 'Madurai, Tamil Nadu',
        'website': 'https://www.thiagarajar.edu/'
    },
    'Madras Institute of Technology': {
        'name': 'Madras Institute of Technology',
        'description': 'Autonomous public technical and research university located in Chennai, Tamil Nadu.',
        'location': 'Chennai, Tamil Nadu',
        'website': 'https://www.mitindia.edu/'
    },
    'Noorul Islam College of Engineering': {
        'name': 'Noorul Islam College of Engineering',
        'description': 'Private engineering college located in Kumarakovil, Tamil Nadu.',
        'location': 'Kumarakovil, Tamil Nadu',
        'website': 'https://www.nice.ac.in/'
    },
    # Add more colleges as needed
}

def get_college_info(query):
    for key in colleges:
        if key.lower() in query.lower():
            college = colleges[key]
            return f"{college['name']}\nDescription: {college['description']}\nLocation: {college['location']}\nWebsite: {college['website']}"
    return "Sorry, I don't have information about that college."
