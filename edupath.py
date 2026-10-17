"""
EduPath - Complete Education & Career Pathway Explorer
------------------------------------------------------
A Python-only, menu-driven education guidance mini-project.

Features:
- Pathways after Class 10, Intermediate, Diploma, and Graduation
- Intermediate groups and technical/vocational routes
- Entrance-exam discovery
- Government institution examples
- Scholarships and fee-support discovery
- Course comparison
- Career and higher-study exploration
- OOP-based design
- No SQL, no third-party packages, and no web framework

Important:
This is an educational prototype with sample data, not an official admission
decision system. Exam rules, dates, fees, scholarships, seat availability, and
eligibility change. Verify every decision with the official authority.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# DATA MODELS
# ---------------------------------------------------------------------------

@dataclass
class Student:
    name: str = ""
    current_level: str = ""
    state: str = "Andhra Pradesh / Telangana"
    interests: List[str] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    budget_preference: str = "Any"
    marks_or_rank: str = ""

    def display_summary(self) -> None:
        print("\n--- Student Profile ---")
        print(f"Name: {self.name or 'Not provided'}")
        print(f"Current qualification: {self.current_level or 'Not selected'}")
        print(f"Preferred state/region: {self.state}")
        print(f"Interests: {', '.join(self.interests) if self.interests else 'Not provided'}")
        print(f"Strengths: {', '.join(self.strengths) if self.strengths else 'Not provided'}")
        print(f"Budget preference: {self.budget_preference}")
        print(f"Marks/rank: {self.marks_or_rank or 'Not provided'}")


@dataclass
class Course:
    course_id: str
    name: str
    level: str
    duration: str
    description: str
    subjects_or_focus: List[str]
    next_options: List[str] = field(default_factory=list)
    eligibility_notes: str = ""
    route_type: str = "Academic"

    def display_details(self) -> None:
        print(f"\n{self.name} [{self.course_id}]")
        print(f"Level: {self.level}")
        print(f"Typical duration: {self.duration}")
        print(f"Type: {self.route_type}")
        print(f"Overview: {self.description}")
        print("Subjects / focus: " + (", ".join(self.subjects_or_focus) or "Not specified"))
        if self.eligibility_notes:
            print(f"Eligibility note: {self.eligibility_notes}")
        if self.next_options:
            print("Possible next steps:")
            for option in self.next_options:
                print(f"  - {option}")


@dataclass
class EntranceExam:
    name: str
    stage: str
    purpose: str
    who_may_consider: str
    next_action: str
    official_source: str
    caution: str = ""

    def display(self) -> None:
        print(f"\n{self.name}")
        print(f"Stage: {self.stage}")
        print(f"Purpose: {self.purpose}")
        print(f"Who may consider it: {self.who_may_consider}")
        print(f"After the exam: {self.next_action}")
        print(f"Official source to verify: {self.official_source}")
        if self.caution:
            print(f"Important: {self.caution}")


@dataclass
class Institution:
    name: str
    institution_type: str
    location: str
    opportunity: str
    admission_route: str
    official_source: str
    caution: str = ""

    def display(self) -> None:
        print(f"\n{self.name}")
        print(f"Type: {self.institution_type}")
        print(f"Location: {self.location}")
        print(f"Opportunity: {self.opportunity}")
        print(f"Admission route: {self.admission_route}")
        print(f"Official source to verify: {self.official_source}")
        if self.caution:
            print(f"Important: {self.caution}")


@dataclass
class Scholarship:
    name: str
    support_type: str
    possible_criteria: str
    where_to_check: str
    documents_to_prepare: List[str]
    caution: str = ""

    def display(self) -> None:
        print(f"\n{self.name}")
        print(f"Support: {self.support_type}")
        print(f"Possible criteria: {self.possible_criteria}")
        print(f"Where to check: {self.where_to_check}")
        print("Possible documents to prepare: " + ", ".join(self.documents_to_prepare))
        if self.caution:
            print(f"Important: {self.caution}")


@dataclass
class Career:
    title: str
    related_study: str
    skills: List[str]
    notes: str

    def display(self) -> None:
        print(f"\n{self.title}")
        print(f"Related study: {self.related_study}")
        print("Useful skills: " + ", ".join(self.skills))
        print(f"Notes: {self.notes}")


# ---------------------------------------------------------------------------
# SAMPLE DATA
# ---------------------------------------------------------------------------

COURSES: Dict[str, Course] = {
    "INT_MPC": Course(
        "INT_MPC", "Intermediate MPC", "After Class 10", "Usually 2 years",
        "A subject group with Mathematics, Physics and Chemistry.",
        ["Mathematics", "Physics", "Chemistry"],
        ["B.Tech / B.E.", "B.Sc. and other eligible degrees", "Relevant entrance exams"],
        "Subject availability and admission rules depend on the board and college."
    ),
    "INT_BIPC": Course(
        "INT_BIPC", "Intermediate BiPC", "After Class 10", "Usually 2 years",
        "A subject group focused on Biology and physical sciences.",
        ["Biology", "Physics", "Chemistry"],
        ["Medical and health-related courses", "Agriculture and life sciences",
         "Pharmacy and other eligible degrees"],
        "Each degree has separate subject, entrance and admission requirements."
    ),
    "INT_MEC": Course(
        "INT_MEC", "Intermediate MEC", "After Class 10", "Usually 2 years",
        "A group commonly combining Mathematics, Economics and Commerce.",
        ["Mathematics", "Economics", "Commerce"],
        ["B.Com", "BBA", "Economics and finance-related degrees"],
        "Available subject combinations vary by institution."
    ),
    "INT_CEC": Course(
        "INT_CEC", "Intermediate CEC", "After Class 10", "Usually 2 years",
        "A group commonly combining Civics, Economics and Commerce.",
        ["Civics", "Economics", "Commerce"],
        ["B.Com", "BBA", "BA and eligible law pathways"],
        "Check the specific degree's subject and admission requirements."
    ),
    "INT_HEC": Course(
        "INT_HEC", "Intermediate HEC", "After Class 10", "Usually 2 years",
        "A humanities-focused group commonly combining History, Economics and Civics.",
        ["History", "Economics", "Civics"],
        ["BA and other eligible degrees", "Social sciences", "Law pathways where eligible"],
        "The actual group and subject list depends on the college."
    ),
    "INT_OTHER": Course(
        "INT_OTHER", "Other Intermediate subject combinations", "After Class 10",
        "Usually 2 years",
        "Other subject combinations offered by recognized boards and colleges.",
        ["Depends on the combination"],
        ["Eligible bachelor's degrees", "Vocational or specialized pathways"],
        "Check the official subject list and future-course prerequisites."
    ),
    "DIPLOMA": Course(
        "DIPLOMA", "Polytechnic Diploma", "After Class 10", "Often 3 years",
        "Technical education with branches such as Computer, ECE, EEE, Mechanical and Civil.",
        ["Branch-specific technical subjects", "Practical training"],
        ["Relevant jobs", "Apprenticeships", "Eligible lateral-entry degree routes"],
        "Duration, branches and lateral-entry rules vary by state and institution.",
        "Technical"
    ),
    "ITI": Course(
        "ITI", "ITI / Industrial Training", "After Class 10", "Often 1–2 years; varies by trade",
        "Practical training in trades such as Electrician, Fitter, COPA and Mechanic.",
        ["Trade-specific practical skills"],
        ["Trade-related jobs", "Apprenticeships", "Further eligible training"],
        "Trade duration, eligibility and recognition must be checked with the institute.",
        "Technical / Vocational"
    ),
    "VOCATIONAL": Course(
        "VOCATIONAL", "Vocational Education", "After Class 10 or as permitted",
        "Varies by course",
        "Job-oriented learning in areas such as business, IT, hospitality, design or agriculture.",
        ["Depends on the program"],
        ["Entry-level work", "Further education", "Additional certifications"],
        "Confirm the awarding body, recognition and minimum entry qualification.",
        "Vocational"
    ),
    "OPEN": Course(
        "OPEN", "Recognized Open Schooling", "After Class 10", "Depends on subjects and pace",
        "A flexible route to continue secondary or senior-secondary education.",
        ["Subjects selected under the board"],
        ["Higher education when eligibility is met", "Vocational pathways"],
        "Check board recognition, subject requirements and target-course eligibility."
    ),
    "BTECH": Course(
        "BTECH", "B.Tech / B.E.", "After eligible Class 12 or diploma route",
        "Usually 4 years from first year",
        "An undergraduate engineering degree with a chosen branch.",
        ["Branch-specific engineering subjects"],
        ["Technical jobs", "M.Tech and other eligible postgraduate study",
         "Professional certifications"],
        "Admission depends on subjects, entrance rules, counselling and seat availability."
    ),
    "BSC": Course(
        "BSC", "B.Sc.", "After eligible Class 12", "Often 3–4 years depending on program",
        "A science degree in a subject such as Mathematics, Physics, Chemistry, Biology or Computing.",
        ["Degree-specific science subjects"],
        ["M.Sc. and other eligible postgraduate study", "Research pathways", "Jobs"],
        "Subject prerequisites and degree duration depend on the university."
    ),
    "HEALTH": Course(
        "HEALTH", "Medical / Health-related degrees", "After eligible Class 12",
        "Varies by degree",
        "A broad category including medicine, dentistry, nursing, pharmacy and allied fields.",
        ["Course-specific science and clinical subjects"],
        ["Professional practice where licensed", "Higher study", "Related careers"],
        "Requirements differ substantially; NEET applies to MBBS and other courses as specified by their rules."
    ),
    "AGRI_LIFE": Course(
        "AGRI_LIFE", "Agriculture / Life Sciences", "After eligible Class 12",
        "Varies by degree",
        "Programs in agriculture, biotechnology, life sciences and related fields.",
        ["Course-specific science subjects"],
        ["Higher studies", "Research", "Industry and field roles"],
        "Check course-specific subject and entrance requirements."
    ),
    "BCOM": Course(
        "BCOM", "B.Com.", "After eligible Class 12", "Often 3–4 years depending on program",
        "A degree focused on commerce, accounting, finance and business.",
        ["Accounting", "Commerce", "Finance"],
        ["M.Com / MBA and other eligible study", "CA/CMA pathways", "Business careers"],
        "Professional qualifications have separate entry and completion requirements."
    ),
    "BBA": Course(
        "BBA", "BBA / Business Administration", "After eligible Class 12",
        "Often 3–4 years depending on program",
        "A degree focused on management, business and organizations.",
        ["Management", "Business", "Economics or related subjects"],
        ["MBA and other eligible study", "Business and management roles"],
        "Admission criteria vary by institution."
    ),
    "BA": Course(
        "BA", "B.A. / Arts and Humanities", "After eligible Class 12",
        "Often 3–4 years depending on program",
        "A degree in areas such as History, Economics, Political Science, Languages or Sociology.",
        ["Chosen humanities or social-science subjects"],
        ["MA and other eligible study", "Teaching after required qualifications",
         "Civil-services preparation and other careers"],
        "Some professional courses require separate prerequisites or entrance exams."
    ),
    "PG": Course(
        "PG", "Postgraduate Study", "After a relevant bachelor's degree",
        "Often 1–3 years depending on program",
        "Further study such as M.Tech, M.Sc., MBA, M.Com, MA or MCA where eligible.",
        ["Depends on the postgraduate program"],
        ["Research", "Specialized roles", "Doctoral study where eligible"],
        "Each program has its own qualifying-degree and entrance requirements."
    ),
    "PHD": Course(
        "PHD", "Research / Ph.D.", "After the required qualifying degree",
        "Varies by program and rules",
        "Advanced research in a chosen field.",
        ["Research methods and subject specialization"],
        ["Research", "Academic careers where qualified", "Specialized industry roles"],
        "Admission requirements vary; a bachelor's degree alone is not sufficient for every route."
    ),
}


EXAMS: List[EntranceExam] = [
    EntranceExam(
        "RGUKT Basar admission process",
        "After Class 10 (when notified)",
        "Admission to the university's integrated technical education program.",
        "Eligible Class 10 students meeting the current notification's criteria.",
        "Read the current notification, submit the application, follow selection instructions and complete admission if selected.",
        "RGUKT Basar official website: https://www.rgukt.ac.in/",
        "Admission method, eligibility, dates and selection rules may change each year."
    ),
    EntranceExam(
        "TG POLYCET",
        "After Class 10",
        "Admission to participating Telangana Polytechnic Diploma programs.",
        "Candidates meeting the current examination and course requirements.",
        "Check the official notification and counselling process.",
        "Official portal: https://tgpolycet.nic.in/",
        "Verify current portal, eligibility, dates and participating colleges."
    ),
    EntranceExam(
        "AP POLYCET",
        "After Class 10",
        "Admission to participating Andhra Pradesh Polytechnic Diploma programs.",
        "Candidates meeting the current examination and course requirements.",
        "Check the current official notification and counselling process.",
        "Use the Andhra Pradesh Department of Technical Education / POLYCET official portal.",
        "Confirm the current official URL from the state government's website."
    ),
    EntranceExam(
        "TG EAPCET",
        "After eligible Intermediate",
        "Admission to participating Telangana engineering and other listed programs.",
        "Candidates who meet the relevant stream, subject and exam requirements.",
        "Check the current notification, result, counselling and seat-allotment rules.",
        "Use the official Telangana EAPCET portal linked by the state government.",
        "Qualifying does not guarantee a seat; rank, eligibility and counselling matter."
    ),
    EntranceExam(
        "AP EAPCET",
        "After eligible Intermediate",
        "Admission to participating Andhra Pradesh engineering, agriculture and pharmacy-related programs as notified.",
        "Candidates who meet the relevant stream and course requirements.",
        "Check the current notification and counselling instructions.",
        "Use the official Andhra Pradesh EAPCET portal linked by the state government.",
        "Courses, eligibility and counselling rules vary."
    ),
    EntranceExam(
        "JEE Main",
        "Usually after / during eligible Class 12",
        "Admission consideration for participating engineering institutions and other programs as specified.",
        "Candidates meeting the current NTA and institution requirements.",
        "Check the current information bulletin, apply through the official portal and follow the relevant admission process.",
        "Official portal: https://jeemain.nta.nic.in/",
        "Institution-specific subject, year, rank and other eligibility rules apply."
    ),
    EntranceExam(
        "NEET-UG",
        "After eligible Class 12",
        "Admission to MBBS and other courses as specified by the current rules.",
        "Candidates meeting the current subject, age and other eligibility requirements.",
        "Check the current information bulletin, apply and follow the applicable counselling process.",
        "Official portal: https://neet.nta.nic.in/",
        "Do not assume NEET is required for every BiPC-related degree."
    ),
    EntranceExam(
        "CUET-UG",
        "After eligible Class 12",
        "Admission to participating universities and programs.",
        "Candidates meeting the selected university's subject and course requirements.",
        "Check the current exam bulletin and each participating university's admission rules.",
        "Official portal: https://cuet.nta.nic.in/",
        "Not all universities or programs use CUET; verify the target course."
    ),
    EntranceExam(
        "State lateral-entry / ECET-type admission",
        "After an eligible Diploma",
        "Potential lateral entry into engineering degree programs where permitted.",
        "Diploma holders meeting the relevant state, branch and other requirements.",
        "Check the current state exam or admission notification and counselling procedure.",
        "Use the official state technical education / lateral-entry admission portal.",
        "Lateral entry is subject to current rules, eligibility, branch mapping and available seats."
    ),
]


INSTITUTIONS: List[Institution] = [
    Institution(
        "RGUKT Basar",
        "Public university / integrated technical education",
        "Basar, Telangana",
        "Integrated technical education opportunity for eligible students after Class 10.",
        "Follow the current official admission notification and selection process.",
        "https://www.rgukt.ac.in/",
        "Do not assume admission is automatic or that every student qualifies."
    ),
    Institution(
        "Government Polytechnic colleges",
        "Government technical education institutions",
        "Andhra Pradesh and Telangana; varies by college",
        "Diploma branches such as Computer, ECE, EEE, Mechanical, Civil and other offered branches.",
        "State Polytechnic entrance/admission process and counselling where applicable.",
        "Check the relevant state technical education department and official counselling portal.",
        "Branches, fees, eligibility and availability vary by college."
    ),
    Institution(
        "Government ITIs",
        "Government vocational / technical training institutions",
        "Andhra Pradesh and Telangana; varies by institute",
        "Approved trade training such as Electrician, Fitter, COPA and other offered trades.",
        "Use the official state ITI admission process.",
        "Check the relevant state ITI / employment and training department website.",
        "Verify trade recognition, duration, eligibility and fees."
    ),
    Institution(
        "Government degree colleges",
        "Public higher education institutions",
        "Andhra Pradesh and Telangana; varies by college",
        "Eligible bachelor's degrees in subjects offered by each college.",
        "Merit, counselling or entrance-based admission as specified by the institution.",
        "Check the state higher education department and the college's official website.",
        "Course availability and admission rules vary."
    ),
    Institution(
        "Government universities and participating public institutions",
        "Public university",
        "Across India",
        "Eligible undergraduate and postgraduate programs.",
        "University-specific or common entrance process where applicable.",
        "Check the university's official admissions page and relevant exam portal.",
        "A public institution does not automatically mean every seat is free."
    ),
]


SCHOLARSHIPS: List[Scholarship] = [
    Scholarship(
        "State post-matric scholarship / fee reimbursement schemes",
        "Possible tuition-fee support or scholarship for eligible students",
        "May depend on domicile, course, income, community/category, institution and other current rules.",
        "Check the official Andhra Pradesh or Telangana scholarship / welfare department portal.",
        ["Identity and domicile documents", "Income certificate if required",
         "Previous academic records", "Admission details", "Bank details where required"],
        "Scheme names, criteria, amounts, renewals and deadlines change; verify current official rules."
    ),
    Scholarship(
        "National Scholarship Portal (NSP) schemes",
        "Scholarships from participating government schemes",
        "Criteria differ by scheme and may include academic, income, category or course requirements.",
        "Official portal: https://scholarships.gov.in/",
        ["Academic records", "Identity details", "Income or category documents if required",
         "Institution verification details"],
        "Not every student or course qualifies; check the individual scheme guidelines."
    ),
    Scholarship(
        "Merit-based institutional scholarships",
        "Possible tuition reduction or financial award",
        "May depend on entrance rank, marks, income, institution policy or other conditions.",
        "Check the institution's official scholarship and fee policy.",
        ["Marks / rank card", "Admission offer", "Income documents if required"],
        "Availability, renewal conditions and amount vary by institution."
    ),
    Scholarship(
        "Hostel and welfare support",
        "Possible hostel, maintenance or other student support",
        "May depend on state, residence, income, category, course and current scheme rules.",
        "Check the relevant state welfare department or institution's official portal.",
        ["Admission details", "Residence or domicile documents if required",
         "Income / other scheme-specific documents"],
        "Support is subject to the current scheme, eligibility and available funding."
    ),
]


CAREERS: List[Career] = [
    Career(
        "Software Developer",
        "Commonly Computer Science / IT / related degrees or equivalent skills",
        ["Programming", "Problem solving", "Data structures", "Software development"],
        "A degree can help with eligibility, but hiring requirements vary by employer."
    ),
    Career(
        "AI / Machine Learning Engineer",
        "Often Computer Science, AI/ML, Mathematics or related study",
        ["Python", "Mathematics", "Statistics", "Machine learning", "Projects"],
        "Usually requires strong technical skills and practical experience."
    ),
    Career(
        "Data Analyst",
        "Various degrees with relevant analytical skills",
        ["Excel", "SQL where used by employers", "Python", "Statistics", "Communication"],
        "This is a career-information example; EduPath itself does not use SQL."
    ),
    Career(
        "Doctor",
        "Required medical qualification and registration",
        ["Biology", "Clinical learning", "Communication", "Professional ethics"],
        "MBBS admission has specific eligibility and entrance requirements; professional registration applies."
    ),
    Career(
        "Pharmacist",
        "Recognized pharmacy qualification and applicable registration",
        ["Pharmaceutical knowledge", "Accuracy", "Communication"],
        "The required qualification and registration depend on the role and regulations."
    ),
    Career(
        "Accountant / Finance Professional",
        "Commerce, accounting, finance or related qualifications",
        ["Accounting", "Numeracy", "Excel", "Attention to detail"],
        "Some roles and professional designations require additional qualifications."
    ),
    Career(
        "Civil / Mechanical / Electrical Engineer",
        "Relevant engineering qualification",
        ["Engineering fundamentals", "Technical tools", "Problem solving"],
        "Branch-specific qualifications and employer requirements apply."
    ),
    Career(
        "Skilled Trade Technician",
        "Relevant ITI / diploma / approved trade qualification",
        ["Practical trade skills", "Safety", "Troubleshooting"],
        "Requirements vary by trade, employer and any required license."
    ),
    Career(
        "Researcher / Lecturer",
        "Relevant subject degree and further qualifications as required",
        ["Subject expertise", "Research", "Communication", "Writing"],
        "Teaching and research roles have specific qualification and recruitment rules."
    ),
]


# Education pathway graph: each ID points to possible next course IDs.
PATHWAYS: Dict[str, List[str]] = {
    "CLASS10": ["INT_MPC", "INT_BIPC", "INT_MEC", "INT_CEC", "INT_HEC",
                "INT_OTHER", "DIPLOMA", "ITI", "VOCATIONAL", "OPEN"],
    "INT_MPC": ["BTECH", "BSC", "BCOM", "BBA", "BA"],
    "INT_BIPC": ["HEALTH", "AGRI_LIFE", "BSC", "BPHARM_PLACEHOLDER"],
    "INT_MEC": ["BCOM", "BBA", "BA"],
    "INT_CEC": ["BCOM", "BBA", "BA"],
    "INT_HEC": ["BA", "BCOM", "BBA"],
    "INT_OTHER": ["BSC", "BCOM", "BBA", "BA"],
    "DIPLOMA": ["BTECH"],
    "ITI": [],
    "VOCATIONAL": [],
    "OPEN": ["INT_MPC", "INT_BIPC", "INT_MEC", "INT_CEC", "INT_HEC", "INT_OTHER"],
    "BTECH": ["PG"],
    "BSC": ["PG"],
    "HEALTH": ["PG"],
    "AGRI_LIFE": ["PG"],
    "BCOM": ["PG"],
    "BBA": ["PG"],
    "BA": ["PG"],
    "PG": ["PHD"],
}

# Remove a placeholder route and keep the list accurate for the prototype.
# Pharmacy options are covered in the Health / BiPC guidance text and exam section.
PATHWAYS["INT_BIPC"] = ["HEALTH", "AGRI_LIFE", "BSC"]


# ---------------------------------------------------------------------------
# APPLICATION SERVICES
# ---------------------------------------------------------------------------

class EligibilityChecker:
    """Provides cautious, preliminary guidance based on recorded information."""

    @staticmethod
    def check_course(course: Course) -> None:
        print("\n--- Eligibility guidance ---")
        print(f"Selected option: {course.name}")
        print(course.eligibility_notes or
              "Check the current official admission notification.")
        print("This prototype does not calculate a final admission decision.")
        print("Confirm subjects, marks, entrance exams, age and other criteria with the authority.")

    @staticmethod
    def explain_exam_limits() -> None:
        print("\nEligibility checks in this prototype are informational only.")
        print("Actual eligibility may depend on subjects, marks, age, domicile,")
        print("category, qualifying year, exam rules, institution rules and other conditions.")


class EducationPathway:
    def __init__(self, courses: Dict[str, Course], pathways: Dict[str, List[str]]):
        self.courses = courses
        self.pathways = pathways

    def display_available(self, course_ids: List[str]) -> List[str]:
        valid_ids = [course_id for course_id in course_ids if course_id in self.courses]
        if not valid_ids:
            print("No pathway data has been added for this option yet.")
            return []
        for index, course_id in enumerate(valid_ids, start=1):
            course = self.courses[course_id]
            print(f"{index}. {course.name} ({course.duration})")
        return valid_ids

    def explore_from(self, start_id: str = "CLASS10") -> None:
        current_id = start_id
        visited: List[str] = []

        while True:
            if current_id == "CLASS10":
                print("\n--- Options after Class 10 ---")
                available = self.display_available(self.pathways["CLASS10"])
            elif current_id in self.courses:
                current_course = self.courses[current_id]
                current_course.display_details()
                EligibilityChecker.check_course(current_course)
                visited.append(current_id)
                next_ids = self.pathways.get(current_id, [])
                if not next_ids:
                    print("\nNo additional pathway has been entered for this course yet.")
                    return
                print("\nExplore the next step:")
                available = self.display_available(next_ids)
            else:
                print("That pathway is not available in the sample data.")
                return

            print("\n0. Go back / finish exploring")
            choice = input("Choose a number: ").strip()
            if choice == "0":
                return
            if not choice.isdigit() or not (1 <= int(choice) <= len(available)):
                print("Invalid choice. Please select one of the displayed numbers.")
                continue
            current_id = available[int(choice) - 1]


class CareerGuidance:
    def __init__(self, student: Student):
        self.student = student

    def collect_profile(self) -> None:
        print("\n--- Optional student profile ---")
        name = input("Student name (optional): ").strip()
        if name:
            self.student.name = name

        print("Preferred region:")
        print("1. Andhra Pradesh")
        print("2. Telangana")
        print("3. Other / All India")
        region_choice = input("Choose 1-3 (default 1): ").strip()
        self.student.state = {
            "1": "Andhra Pradesh",
            "2": "Telangana",
            "3": "Other / All India",
        }.get(region_choice, self.student.state)

        interests = input(
            "Interests separated by commas (e.g. computers, medicine, business): "
        ).strip()
        if interests:
            self.student.interests = [item.strip() for item in interests.split(",") if item.strip()]

        strengths = input(
            "Subject strengths separated by commas (optional): "
        ).strip()
        if strengths:
            self.student.strengths = [item.strip() for item in strengths.split(",") if item.strip()]

        print("Budget preference:")
        print("1. Lowest possible cost")
        print("2. Scholarships / financial support")
        print("3. Any")
        budget_choice = input("Choose 1-3 (default 3): ").strip()
        self.student.budget_preference = {
            "1": "Lowest possible cost",
            "2": "Scholarships / financial support",
            "3": "Any",
        }.get(budget_choice, "Any")

        self.student.display_summary()

    def recommend_general_directions(self) -> None:
        print("\n--- General exploration suggestions ---")
        interests = [item.lower() for item in self.student.interests]
        if any(word in interest for interest in interests for word in
               ["computer", "coding", "software", "ai", "technology"]):
            print("- Explore computing, engineering, IT, science and related eligible pathways.")
        if any(word in interest for interest in interests for word in
               ["medical", "biology", "doctor", "health", "pharmacy"]):
            print("- Explore BiPC-related, health, pharmacy, agriculture and life-science pathways.")
        if any(word in interest for interest in interests for word in
               ["business", "commerce", "account", "finance"]):
            print("- Explore commerce, business, accounting, economics and finance pathways.")
        if any(word in interest for interest in interests for word in
               ["history", "society", "law", "government", "politics"]):
            print("- Explore humanities, social sciences, law and public-service pathways.")
        if any(word in interest for interest in interests for word in
               ["machine", "electrical", "mechanic", "practical", "technical"]):
            print("- Explore Polytechnic, ITI, vocational and engineering-related pathways.")
        if not self.student.interests:
            print("- Add your interests to your profile to see broad suggestions.")
        print("These are exploration suggestions, not an automated eligibility decision.")


class EduPathApp:
    def __init__(self):
        self.student = Student()
        self.pathway = EducationPathway(COURSES, PATHWAYS)
        self.guidance = CareerGuidance(self.student)

    @staticmethod
    def pause() -> None:
        input("\nPress Enter to continue...")

    @staticmethod
    def choose_from_list(title: str, items: List[object], display_method: str) -> None:
        print(f"\n--- {title} ---")
        if not items:
            print("No entries are available.")
            return
        for index, item in enumerate(items, start=1):
            if isinstance(item, Course):
                print(f"{index}. {item.name}")
            elif isinstance(item, EntranceExam):
                print(f"{index}. {item.name}")
            elif isinstance(item, Institution):
                print(f"{index}. {item.name}")
            elif isinstance(item, Scholarship):
                print(f"{index}. {item.name}")
            elif isinstance(item, Career):
                print(f"{index}. {item.title}")
        print("0. Back to main menu")

        while True:
            choice = input("Choose an item number: ").strip()
            if choice == "0":
                return
            if not choice.isdigit() or not 1 <= int(choice) <= len(items):
                print("Invalid choice. Try again.")
                continue
            selected = items[int(choice) - 1]
            getattr(selected, display_method)()
            return

    def show_course_catalog(self) -> None:
        ids = list(COURSES.keys())
        print("\n--- Course Catalog ---")
        for index, course_id in enumerate(ids, start=1):
            print(f"{index}. {COURSES[course_id].name}")
        print("0. Back")
        while True:
            choice = input("Choose a course to view details: ").strip()
            if choice == "0":
                return
            if not choice.isdigit() or not 1 <= int(choice) <= len(ids):
                print("Invalid choice. Try again.")
                continue
            course = COURSES[ids[int(choice) - 1]]
            course.display_details()
            EligibilityChecker.check_course(course)
            self.pause()
            return

    def show_exams(self) -> None:
        print("\n--- Entrance Exams ---")
        print("Choose an exam to see its purpose and next steps.")
        self.choose_from_list("Exam list", EXAMS, "display")

    def show_institutions(self) -> None:
        self.choose_from_list("Government / Public Institution Examples",
                              INSTITUTIONS, "display")

    def show_scholarships(self) -> None:
        self.choose_from_list("Scholarships and Financial Support",
                              SCHOLARSHIPS, "display")

    def show_careers(self) -> None:
        self.choose_from_list("Career Explorer", CAREERS, "display")

    def compare_courses(self) -> None:
        course_ids = list(COURSES.keys())
        print("\n--- Compare Two Courses ---")
        for index, course_id in enumerate(course_ids, start=1):
            print(f"{index}. {COURSES[course_id].name}")
        selected: List[Course] = []

        for label in ("first", "second"):
            while True:
                choice = input(f"Choose the {label} course number: ").strip()
                if not choice.isdigit() or not 1 <= int(choice) <= len(course_ids):
                    print("Invalid number. Try again.")
                    continue
                selected.append(COURSES[course_ids[int(choice) - 1]])
                break

        print("\n--- Comparison ---")
        for course in selected:
            print(f"\n{course.name}")
            print(f"Level: {course.level}")
            print(f"Duration: {course.duration}")
            print(f"Type: {course.route_type}")
            print(f"Focus: {', '.join(course.subjects_or_focus)}")
            print(f"Next options: {', '.join(course.next_options) or 'Not listed'}")
        print("\nFees, admission difficulty and eligibility must be verified separately.")

    def main_menu(self) -> None:
        while True:
            print("\n" + "=" * 62)
            print("  EduPath - Complete Education & Career Pathway Explorer")
            print("=" * 62)
            print("1. Explore options after Class 10")
            print("2. Explore options after Intermediate")
            print("3. Explore options after Polytechnic / Diploma")
            print("4. Explore options after Graduation")
            print("5. Browse all courses")
            print("6. Find entrance exams")
            print("7. Find government / public institutions")
            print("8. Find scholarships and fee support")
            print("9. Explore careers")
            print("10. Compare two courses")
            print("11. Create / view student profile")
            print("0. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.pathway.explore_from("CLASS10")
                self.pause()
            elif choice == "2":
                print("\nSelect your Intermediate group:")
                group_ids = ["INT_MPC", "INT_BIPC", "INT_MEC", "INT_CEC", "INT_HEC", "INT_OTHER"]
                for i, course_id in enumerate(group_ids, start=1):
                    print(f"{i}. {COURSES[course_id].name}")
                print("0. Back")
                group_choice = input("Choose a group: ").strip()
                if group_choice.isdigit() and 1 <= int(group_choice) <= len(group_ids):
                    self.pathway.explore_from(group_ids[int(group_choice) - 1])
                elif group_choice != "0":
                    print("Invalid choice.")
                self.pause()
            elif choice == "3":
                self.pathway.explore_from("DIPLOMA")
                self.pause()
            elif choice == "4":
                self.pathway.explore_from("PG")
                self.pause()
            elif choice == "5":
                self.show_course_catalog()
            elif choice == "6":
                self.show_exams()
                self.pause()
            elif choice == "7":
                self.show_institutions()
                self.pause()
            elif choice == "8":
                self.show_scholarships()
                self.pause()
            elif choice == "9":
                self.show_careers()
                self.pause()
            elif choice == "10":
                self.compare_courses()
                self.pause()
            elif choice == "11":
                self.guidance.collect_profile()
                self.guidance.recommend_general_directions()
                self.pause()
            elif choice == "0":
                print("\nThank you for using EduPath. Good luck with your education journey!")
                break
            else:
                print("Invalid choice. Enter a number from the menu.")


def main() -> None:
    print("Welcome to EduPath!")
    print("Explore education, entrance exams, public institutions and careers.")
    print("This is a sample guide. Always verify official admission rules.")
    app = EduPathApp()
    app.main_menu()


if __name__ == "__main__":
    main()
