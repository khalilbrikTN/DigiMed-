import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link, useNavigate, useLocation } from 'react-router-dom';
import './App.css'; // Assuming you have an external CSS file for styling
import DatePicker from 'react-datepicker'; // You need to install this library: `npm install react-datepicker`
import 'react-datepicker/dist/react-datepicker.css'; // Import DatePicker styles
// Login Screen
const medicalRecord = {
  patientName: "Omar Omar",
  dateOfBirth: "2005-05-25",
  allergies: ["Peanuts", "Carrots"],
  medicalConditions: [
    {
      medCondition: "Hypertension",
      notes: "Monitor blood pressure regularly.",
    },
    {
      medCondition: "Diabetes",
      notes: "Diet and exercise recommended to manage blood sugar levels.",
    },
    {
      medCondition: "Asthma",
      notes: "Use inhaler during attacks and avoid triggers.",
    },
  ],
  medicalTests: [
    {
      testType: "Blood Test",
      subjectOfTest: "Blood Sugar Levels",
      result: "Normal",
      imageOfScan: "blood_test_image.jpg",
      dateTimeOfUpload: "2024-11-01T10:30:00",
    },
    {
      testType: "X-ray",
      subjectOfTest: "Chest X-ray",
      result: "Clear",
      imageOfScan: "chest_xray_image.jpg",
      dateTimeOfUpload: "2024-11-01T11:00:00",
    },
    {
      testType: "MRI",
      subjectOfTest: "Brain MRI",
      result: "No abnormalities detected.",
      imageOfScan: "brain_mri_image.jpg",
      dateTimeOfUpload: "2024-11-01T12:00:00",
    },
  ],
  prescriptions: [
    {
      doctorName: "Dr. Ali Ahmed",
      dateOfPrescription: "2024-10-15",
      medicines: [
        {
          medicineName: "Panadol",
          subscriptionHeading: "For pain relief",
          formOfIntake: "Tablet",
          durationOfIntake: 30, // in days
          frequencyOfIntake: "Once daily",
          sideEffects: "Headache, Muscle pain",
        },
        {
          medicineName: "Paracetamol",
          subscriptionHeading: "For fever",
          formOfIntake: "Tablet",
          durationOfIntake: 15, // in days
          frequencyOfIntake: "Twice daily",
          sideEffects: "Nausea, Dizziness",
        },
      ],
    },
    {
      doctorName: "Dr. Laila Hassan",
      dateOfPrescription: "2024-11-01",
      medicines: [
        {
          medicineName: "Metformin",
          subscriptionHeading: "For diabetes management",
          formOfIntake: "Tablet",
          durationOfIntake: 60, // in days
          frequencyOfIntake: "Twice daily",
          sideEffects: "Nausea, Diarrhea",
        },
      ],
    },
    {
      doctorName: "Dr. Salma Swelam",
      dateOfPrescription: "2024-11-01",
      medicines: [
        {
          medicineName: "Augmentin",
          subscriptionHeading: "For infection",
          formOfIntake: "Tablet",
          durationOfIntake: 60, // in days
          frequencyOfIntake: "Twice daily",
          sideEffects: "Nausea, Diarrhea",
        },
      ],
    },
  ],
};
function LoginScreen() {
  const [password, setPassword] = useState('');
  const [name, setUserName] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    navigate('/home', { state: { userName: name } });
  };

  return (
    <div className="container">
      <h1 className="title">Welcome to DigiMed!</h1>
      <h2 className="subtitle">Login to your account.</h2>
      <input
        className="input"
        placeholder="Enter your user name"
        value={name}
        onChange={(e) => setUserName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Enter your Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        type="password"
      />
      <Link to="/forgot-password" className="forgotPasswordText">Forgot password?</Link>
      <button className="button" onClick={handleLogin}>Login</button>
      <Link to="/signup" className="signupText">Don’t have an account? Sign up</Link>
    </div>
  );
}

// Signup Screen
function SignupScreen() {
  const [firstName, setFirstName] = useState('');
  const [middleName, setMiddleName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [email, setEmail] = useState('');
  const [dob, setDob] = useState('');
  const [street, setStreet] = useState('');
  const [region, setRegion] = useState('');
  const [city, setCity] = useState('');
  const [gender, setGender] = useState('');
  const [bloodType, setBloodType] = useState('');
  const [height, setHeight] = useState('');
  const [weight, setWeight] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const handleSignup = () => {
    // Call backend API to save the data and navigate to the home screen
    navigate('/home', { state: { userName: firstName } });
  };

  return (
    <div className="container">
      <h1 className="title">Welcome to DigiMed!</h1>
      <h2 className="subtitle">Sign up to your account.</h2>

      <input
        className="input"
        placeholder="First Name"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Middle Name (optional)"
        value={middleName}
        onChange={(e) => setMiddleName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Last Name"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Phone Number"
        value={phoneNumber}
        onChange={(e) => setPhoneNumber(e.target.value)}
        type="tel"
      />
      <input
        className="input"
        placeholder="Email Address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        type="email"
      />
      <input
        className="input"
        placeholder="Date of Birth"
        value={dob}
        onChange={(e) => setDob(e.target.value)}
        type="date"
      />
      <input
        className="input"
        placeholder="Street Address"
        value={street}
        onChange={(e) => setStreet(e.target.value)}
      />
      <input
        className="input"
        placeholder="Region"
        value={region}
        onChange={(e) => setRegion(e.target.value)}
      />
      <input
        className="input"
        placeholder="City"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <select
        className="input"
        value={gender}
        onChange={(e) => setGender(e.target.value)}
      >
        <option value="">Select Gender</option>
        <option value="M">Male</option>
        <option value="F">Female</option>
      </select>
      <input
        className="input"
        placeholder="Blood Type"
        value={bloodType}
        onChange={(e) => setBloodType(e.target.value)}
      />
      <input
        className="input"
        placeholder="Height (in cm)"
        value={height}
        onChange={(e) => setHeight(e.target.value)}
        type="number"
      />
      <input
        className="input"
        placeholder="Weight (in kg)"
        value={weight}
        onChange={(e) => setWeight(e.target.value)}
        type="number"
      />
      <input
        className="input"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button className="button" onClick={handleSignup}>
        Sign Up
      </button>
    </div>
  );
}

// Home Screen
function HomeScreen() {
    const location = useLocation();
    const userName = location.state?.userName || 'User';
    const navigate = useNavigate();
  
    // Get medical records and appointments from location/state or mock data
    const upcomingAppointments = sampleAppointments.filter((sampleAppointment) => sampleAppointment.status === 'Upcoming');

    // Medication reminders (from prescriptions)
    const medicationReminders = medicalRecord.prescriptions.flatMap((prescription) =>
      prescription.medicines.map((medicine) => ({
        name: medicine.medicineName,
        frequency: medicine.frequencyOfIntake,
        duration: medicine.durationOfIntake,
      }))
    );
    return (
      <div className="homeContainer">
        <h2 className="welcomeText">Welcome Back, User</h2>
        <div className="sectionDivider"></div>
  
        <div className="upperSection">
          <div className="profileIconContainer">
            <img src="src/download.png" alt="Profile" className="profileIcon" />
          </div>
          <div className="upperButtonsContainer">
            <button className="widgetButton" onClick={() => navigate('/manage-profile')}>Manage Profile</button>
            <button className="widgetButton" onClick={() => navigate('/view-appointments')}>View Appointments</button>
          </div>
        </div>
  
        <div className="sectionDivider"></div>
  
        <div className="lowerSection">
          <div className="lowerButtonsRow">
            <button className="lowerWidgetButton" onClick={() => navigate('/doctor-selection')}>Scheduling</button>
            <button className="lowerWidgetButton" onClick={() => navigate('/medical-records')}>Medical Records</button>
          </div>
  
          <div className="lowerButtonsRow">
            <div className="infoWidget">
              <h3 className="widgetTitle">Upcoming Appointments</h3>
              <div className="appointmentList">
                {upcomingAppointments.length > 0 ? (
                  upcomingAppointments.map((appointment) => (
                    <div key={appointment.id} className="appointmentItem">
                      <p className="appointmentDate"><span className="subtitle">Date:</span> {appointment.date}</p>
                      <p className="appointmentTime"><span className="subtitle">Time:</span> {appointment.time}</p>
                      <p className="appointmentDoctor"><span className="subtitle">Doctor:</span> {appointment.doctor.name}</p>
                    </div>
                  ))
                ) : (
                  <p>No upcoming appointments.</p>
                )}
              </div>
            </div>
  
            <div className="infoWidget">
              <h3 className="widgetTitle">Medication Reminders</h3>
              <div className="medicationList">
                {medicationReminders.length > 0 ? (
                  medicationReminders.map((reminder, index) => (
                    <div key={index} className="medicationItem">
                      <p className="medicationName"><span className="subtitle">Medicine:</span> {reminder.name}</p>
                      <p className="medicationDetails"><span className="subtitle">Frequency:</span> {reminder.frequency} for {reminder.duration} days</p>
                    </div>
                  ))
                ) : (
                  <p>No medication reminders.</p>
                )}
              </div>
            </div>
          </div>
        </div>
  
        <div className="sectionDivider"></div>
        <button className="logoutButton" onClick={() => navigate('/')}>Log Out</button>
      </div>
    );
  };
  

// Doctor Selection Screen
function DoctorSelectionScreen() {
  const [selectedDoctor, setSelectedDoctor] = useState(null);
  const navigate = useNavigate();

  const doctors = [
    { 
      id: 1, 
      first_name: 'Ahmed', 
      middle_name: 'Fawzy', 
      last_name: '', 
      specialty: 'Dermato-Endocrinology', 
      sub_specialty: 'Endocrine Disorders', 
      //rating: 5,  not in datamodel 
      //reviews: 60 
    },
    { 
      id: 2, 
      first_name: 'Hoda', 
      middle_name: 'Magdy', 
      last_name: '', 
      specialty: 'Dermato-Genetics', 
      sub_specialty: 'Genetic Skin Conditions', 
      //rating: 4.5, 
      //reviews: 40 
    },
    { 
      id: 3, 
      first_name: 'Yasmina', 
      middle_name: 'Mahdy', 
      last_name: '', 
      specialty: 'Cosmetic Bioengineering', 
      sub_specialty: 'Aesthetic Enhancements', 
      //rating: 5, 
      //reviews: 150 
    },
    { 
      id: 4, 
      first_name: 'Mohamed', 
      middle_name: 'Kahil', 
      last_name: '', 
      specialty: 'Nano-Dermatology', 
      sub_specialty: 'Nano-Technology in Dermatology', 
      //rating: 4.8, 
      //reviews: 90 
    },
  ];

  const handleDoctorClick = (doctor) => {
    navigate('/doctor-details', { state: { doctor } });
  };

  return (
    <div className="doctorSelectionContainer">
      <div className="doctorSelectionHeader">
        <div>
          <h1>Welcome Back</h1>
       
        </div>
        <img src="src/download.png" alt="Profile" className="profileIcon" />
      </div>

      <div className="doctorSelectionSearchContainer">
        <div className="doctorSelectionTab">Doctors</div>
        <div className="doctorSelectionTab">Favorites</div>
        <div className="doctorSelectionSearchBar">
          <input type="text" placeholder="Search..." className="doctorSelectionSearchInput" />
        </div>
      </div>

      {doctors.map((doctor) => (
        <div key={doctor.id} className="doctor-card" onClick={() => handleDoctorClick(doctor)}>
          <div className="doctor-image-container">
            <img
              src="src/download.png"
              alt="profile"
              className="profileIcon"
            />
          </div>
          <div className="doctor-info-container">
            <h3 className="doctor-name">
              {doctor.first_name} {doctor.middle_name} {doctor.last_name}
            </h3>
            <p className="doctor-specialty">
              {doctor.specialty} - {doctor.sub_specialty}
            </p>

          </div>
          <span className="info-icon">ℹ️</span>
        </div>
      ))}
    </div>
  );
};


// Doctor Details, Date Selection, Time Selection, and Confirmation Screen omitted for brevity (same as above)


const DoctorDetailsScreen = () => {
  const location = useLocation();
  const { doctor } = location.state;
  const navigate = useNavigate();

  return (
    <div className="detailsContainer">
      <img
        className="largeDoctorImage"
        src="src/download.png"
        alt={`${doctor.first_name} ${doctor.last_name}`}
      />
      <h2 className="doctorName">
        {doctor.first_name} {doctor.middle_name} {doctor.last_name}
      </h2>
      <p className="specialty">{doctor.specialty}</p>
      <p className="sub-specialty">{doctor.sub_specialty}</p>
      <button
        className="button"
        onClick={() => navigate('/date-selection', { state: { doctor } })}
      >
        Book Appointment
      </button>
    </div>
  );
};
// Date Selection Screen
function DateSelectionScreen() {
  const location = useLocation();
  const { doctor } = location.state;
  const [selectedDate, setSelectedDate] = useState(null);
  const navigate = useNavigate();

  return (
    <div className="container">
      <h2 className="title">Select a Date with {doctor.name}</h2>
      {/* Replace this Calendar with a date picker library if necessary */}
      <input
        type="date"
        className="datePicker"
        onChange={(e) => setSelectedDate(e.target.value)}
      />
      <button
        className="button"
        disabled={!selectedDate}
        onClick={() => navigate('/time-selection', { state: { doctor, selectedDate } })}
      >
        Next
      </button>
    </div>
  );
}

// Time Slot Selection Screen
function TimeSelectionScreen() {
  const location = useLocation();
  const { doctor, selectedDate } = location.state;
  const availableTimes = ['10:00 AM', '11:00 AM', '1:00 PM', '3:00 PM', '4:30 PM'];
  const [selectedTime, setSelectedTime] = useState(null);
  const navigate = useNavigate();

  return (
    <div className="container">
      <h2 className="title">Available Times on {selectedDate}</h2>
      <div className="timeSlots">
        {availableTimes.map((time) => (
          <button
            key={time}
            className={`timeSlot ${selectedTime === time ? 'selectedTimeSlot' : ''}`}
            onClick={() => setSelectedTime(time)}
          >
            {time}
          </button>
        ))}
      </div>
      <button
        className="button"
        disabled={!selectedTime}
        onClick={() =>
          navigate('/confirmation', { state: { doctor, selectedDate, selectedTime } })
        }
      >
        Confirm Appointment
      </button>
    </div>
  );
}

// Confirmation Screen
function ConfirmationScreen() {
  const location = useLocation();
  const { doctor, selectedDate, selectedTime } = location.state;
  const navigate = useNavigate();

  const handleFinish = () => {
    alert('Your appointment is confirmed!');
    navigate('/home');
  };

  return (
    <div className="container">
      <h2 className="title">Appointment Confirmation</h2>
      <p>Doctor: {doctor.name}</p>
      <p>Specialty: {doctor.specialty}</p>
      <p>Date: {selectedDate}</p>
      <p>Time: {selectedTime}</p>
      <button className="button" onClick={handleFinish}>
        Finish
      </button>
    </div>
  );
}

function ManageProfileScreen() {
  const [firstName, setFirstName] = useState('');
  const [middleName, setMiddleName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [email, setEmail] = useState('');
  const [dob, setDob] = useState('');
  const [street, setStreet] = useState('');
  const [region, setRegion] = useState('');
  const [city, setCity] = useState('');
  const [gender, setGender] = useState('');
  const [bloodType, setBloodType] = useState('');
  const [height, setHeight] = useState('');
  const [weight, setWeight] = useState('');

  return (
    <div className="container">
      <h1 className="title">Profile</h1>
      <div className="profileIconContainer">
        <img
          src="src/download.png" // Ensure the image path is correct
          alt="Profile"
          className="profileIcon"
        />
      </div>
      <input
        className="input"
        placeholder="Edit First Name"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Middle Name (optional)"
        value={middleName}
        onChange={(e) => setMiddleName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Last Name"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Phone Number"
        value={phoneNumber}
        onChange={(e) => setPhoneNumber(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Date of Birth"
        value={dob}
        onChange={(e) => setDob(e.target.value)}
        type="date"
      />
      <input
        className="input"
        placeholder="Edit Street Address"
        value={street}
        onChange={(e) => setStreet(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Region"
        value={region}
        onChange={(e) => setRegion(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit City"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <select
        className="input"
        value={gender}
        onChange={(e) => setGender(e.target.value)}
      >
        <option value="">Select Gender</option>
        <option value="M">Male</option>
        <option value="F">Female</option>
      </select>
      <input
        className="input"
        placeholder="Edit Blood Type"
        value={bloodType}
        onChange={(e) => setBloodType(e.target.value)}
      />
      <input
        className="input"
        placeholder="Edit Height (in cm)"
        value={height}
        onChange={(e) => setHeight(e.target.value)}
        type="number"
      />
      <input
        className="input"
        placeholder="Edit Weight (in kg)"
        value={weight}
        onChange={(e) => setWeight(e.target.value)}
        type="number"
      />

      <button className="button" onClick={() => alert('Changes Saved!')}>
        Save Changes
      </button>
    </div>
  );
}


const sampleAppointments = [
  { id: 1, doctor: { name: "Dr. Rana Taher", specialty: "Dermatologist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Complete" },
  { id: 2, doctor: { name: "Dr. Youssef Farid", specialty: "Oncologist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Complete" },
  { id: 3, doctor: { name: "Dr. Yasmina Mahdy", specialty: "Psychiatrist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Complete" },
  { id: 4, doctor: { name: "Dr. Mostafa Youssef", specialty: "Dermatologist" }, date: "Sunday, 12 June", time: "9:30 AM - 10:00 AM", status: "Upcoming" },
  { id: 5, doctor: { name: "Dr. Ahmed Fawzy", specialty: "Oncologist" }, date: "Sunday, 12 June", time: "9:30 AM - 10:00 AM", status: "Upcoming" },
  { id: 6, doctor: { name: "Dr. Mohamed Khalil", specialty: "Psychiatrist" }, date: "Sunday, 12 June", time: "9:30 AM - 10:00 AM", status: "Upcoming" },
  { id: 7, doctor: { name: "Dr. Sara El Said", specialty: "Cardiologist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Cancelled" },
];

const AppointmentDetails = () => {
  const location = useLocation();
  const appointment = location.state?.appointment;

  if (!appointment) {
    return <div>No appointment details available.</div>;
  }

  // Correct way to render doctor properties
  return (
    <div className="details-container">
      <h2>Appointment Details</h2>
      <p><strong>Doctor:</strong> {appointment.doctor?.name}</p>
      <p><strong>Specialty:</strong> {appointment.doctor?.specialty}</p>
      <p><strong>Date:</strong> {appointment.date}</p>
      <p><strong>Time:</strong> {appointment.time}</p>
      <p><strong>Location:</strong> Not Available</p>
      <p><strong>Notes:</strong> No additional notes</p>
      <Link to="/" className="btn">Back to Appointments</Link>
    </div>
  );
};

function ViewAppointmentsScreen() {
  const navigate = useNavigate();
  const [selectedTab, setSelectedTab] = useState('Upcoming');

  // Filter appointments based on selected tab
  const filteredAppointments = sampleAppointments.filter(appointment => appointment.status === selectedTab);

  return (
    <div className="viewappointment_mainContainer">
      {/* Header */}
      <h1 className="viewappointment_heading">All Appointments</h1>

      {/* Tabs */}
      <div className="viewappointment_tabs">
        {['Upcoming', 'Complete', 'Cancelled'].map((tab) => (
          <button
            key={tab}
            className={`viewappointment_tabButton ${selectedTab === tab ? 'viewappointment_tabButtonActive' : ''}`}
            onClick={() => setSelectedTab(tab)}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Appointment List */}
      <div className="viewappointment_scrollContainer">
        {filteredAppointments.length > 0 ? (
          filteredAppointments.map((appointment) => (
            <div key={appointment.id} className="viewappointment_cardContainer">
              <div className="viewappointment_doctorInfo">
                {/* Correct way to render doctor properties */}
                <h3 className="viewappointment_doctorName">{appointment.doctor?.name}</h3>
                <p className="viewappointment_specialty">{appointment.doctor?.specialty}</p>
                <p className="viewappointment_date">{appointment.date}</p>
                <p className="viewappointment_time">{appointment.time}</p>
              </div>

              {/* Action Buttons */}
              <div className="viewappointment_buttonContainer">
                {selectedTab === 'Upcoming' && (
                  <>
                    <button
                      className="viewappointment_detailsButton"
                      onClick={() => navigate('/details', { state: { appointment } })}
                    >
                      Details
                    </button>
                    <button
                      className="viewappointment_cancelButton"
                      onClick={() => alert('Appointment canceled!')}
                    >
                      Cancel
                    </button>
                  </>
                )}
                {selectedTab === 'Complete' && (
                  <>
                    <button
                      className="viewappointment_rebookButton"
                      onClick={() => navigate('/rebook', { state: { appointment } })}
                    >
                      Re-Book
                    </button>
                    <button
                      className="viewappointment_addReviewButton"
                      onClick={() => navigate('/review', { state: { appointment } })}
                    >
                      Add Review
                    </button>
                  </>
                )}
                {selectedTab === 'Cancelled' && (
                  <button
                    className="viewappointment_addReviewButton"
                    onClick={() => navigate('/review', { state: { appointment } })}
                  >
                    Add Review
                  </button>
                )}
              </div>
            </div>
          ))
        ) : (
          <p>No appointments in this category.</p>
        )}
      </div>
    </div>
  );
}


function DetailsScreen() {
  const navigate = useNavigate();
  const location = useLocation();
  const { appointment } = location.state; // Get appointment details passed as state

  return (
    <div style={{ padding: '30px', maxWidth: '800px', margin: '0 auto', backgroundColor: '#f9f9f9', borderRadius: '8px' }}>
      <h1 style={{ fontSize: '28px', fontWeight: 'bold', marginBottom: '20px', color: '#333' }}>Appointment Details</h1>
      <div style={{ marginBottom: '20px', lineHeight: '1.8' }}>
        {/* Render individual properties of the doctor object */}
        <p><strong>Doctor:</strong> {appointment.doctor?.name}</p>
        <p><strong>Specialty:</strong> {appointment.doctor?.specialty}</p>
        <p><strong>Date:</strong> {appointment.date}</p>
        <p><strong>Time:</strong> {appointment.time}</p>
        <p><strong>Location:</strong> {appointment.location || 'Not specified'}</p>
        <p><strong>Notes:</strong> {appointment.notes || 'No additional notes'}</p>
      </div>
      <button
        onClick={() => navigate(-1)}
        style={{
          padding: '10px 20px',
          backgroundColor: '#007bff',
          color: '#fff',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
          fontWeight: 'bold',
        }}
      >
        Back to Appointments
      </button>
    </div>
  );
}

function CancelScreen() {
  const navigate = useNavigate();
  const location = useLocation();
  const { appointment } = location.state; // Get the full appointment object
  const [reason, setReason] = useState('');

  const handleCancel = () => {
    alert(`Appointment with Dr. ${appointment.doctor?.name} cancelled for reason: ${reason}`);
    navigate(-1); // Go back to the previous screen
  };

  return (
    <div style={{ padding: 16 }}>
      <h1>Cancel Appointment</h1>
      <p>Appointment ID: {appointment.id}</p>
      <p>Doctor: {appointment.doctor?.name}</p>
      <textarea
        placeholder="Enter reason for cancellation"
        style={{ marginTop: '20px', padding: '10px', width: '100%', height: '100px', border: '1px solid #ccc' }}
        value={reason}
        onChange={(e) => setReason(e.target.value)}
      />
      <button
        onClick={handleCancel}
        style={{
          marginTop: '20px',
          padding: '10px 20px',
          backgroundColor: '#f44336',
          color: '#fff',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
        }}
      >
        Confirm Cancellation
      </button>
    </div>
  );
}

function ReviewScreen() {
  const navigate = useNavigate();
  const location = useLocation();
  const { appointment } = location.state; // Get the full appointment object
  const [review, setReview] = useState('');

  const handleReviewSubmit = () => {
    alert(`Review submitted for Appointment with Dr. ${appointment.doctor?.name}: ${review}`);
    navigate(-1); // Go back to the previous screen
  };

  return (
    <div style={{ padding: 16 }}>
      <h1>Add Review</h1>
      <p>Appointment ID: {appointment.id}</p>
      <p>Doctor: {appointment.doctor?.name}</p>
      <textarea
        placeholder="Write your review here"
        style={{ marginTop: '20px', padding: '10px', width: '100%', height: '100px', border: '1px solid #ccc' }}
        value={review}
        onChange={(e) => setReview(e.target.value)}
      />
      <button
        onClick={handleReviewSubmit}
        style={{
          marginTop: '20px',
          padding: '10px 20px',
          backgroundColor: '#4CAF50',
          color: '#fff',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
        }}
      >
        Submit Review
      </button>
    </div>
  );
}
function RebookScreen() {
  const navigate = useNavigate();
  const location = useLocation();
  const { appointment } = location.state; // Get the full appointment object

  const [selectedDate, setSelectedDate] = useState('');
  const [selectedTime, setSelectedTime] = useState('');
  const availableTimeSlots = [
    "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM",
  ];

  const handleConfirm = () => {
    if (selectedDate && selectedTime) {
      alert(`Appointment Rebooked on ${selectedDate} at ${selectedTime}`);
      navigate('/'); // Go back to the home screen after rebooking
    } else {
      alert('Please select both a date and a time slot.');
    }
  };

  return (
    <div className="rebook-container">
      <h2 className="rebook-heading">Rebook Appointment</h2>
      <p>Appointment ID: {appointment.id}</p>
      <p>Doctor: {appointment.doctor?.name}</p>

      <label className="label">
        Select Date:
        <input
          type="date"
          className="date-picker"
          value={selectedDate}
          onChange={(e) => setSelectedDate(e.target.value)}
        />
      </label>

      <div className="time-slots-container">
        <p className="time-slots-heading">Available Time Slots:</p>
        <div className="time-slots">
          {availableTimeSlots.map((slot) => (
            <button
              key={slot}
              className={`time-slot ${selectedTime === slot ? 'active' : ''}`}
              onClick={() => setSelectedTime(slot)}
            >
              {slot}
            </button>
          ))}
        </div>
      </div>

      <button className="confirm-button" onClick={handleConfirm}>
        Confirm Appointment
      </button>
      <button className="back-button" onClick={() => navigate(-1)}>
        Back
      </button>
    </div>
  );
}

const MedicalRecordsScreen = () => {
  const [expandedVisitIndex, setExpandedVisitIndex] = useState(null);
  const [expandedPrescriptionIndex, setExpandedPrescriptionIndex] = useState({});
  const [expandedConditionIndex, setExpandedConditionIndex] = useState(null);
  const [expandedTestIndex, setExpandedTestIndex] = useState(null);

  const toggleVisitExpand = (index) => {
    setExpandedVisitIndex(expandedVisitIndex === index ? null : index);
  };

  const togglePrescriptionExpand = (visitIndex, prescIndex) => {
    setExpandedPrescriptionIndex((prevState) => ({
      ...prevState,
      [visitIndex]: prevState[visitIndex] === prescIndex ? null : prescIndex,
    }));
  };

  const toggleConditionExpand = (index) => {
    setExpandedConditionIndex(expandedConditionIndex === index ? null : index);
  };

  const toggleTestExpand = (index) => {
    setExpandedTestIndex(expandedTestIndex === index ? null : index);
  };

  

  return (
    <div className="rec-container">
      {/* Header Section */}
      <div className="rec-header">
        <h1 className="rec-header-text">Medical Record</h1>
      </div>

      {/* Patient Info */}
      <div className="rec-section">
        <h2 className="rec-section-header">Patient Information</h2>
        <p className="rec-info-text">Name: {medicalRecord.patientName}</p>
        <p className="rec-info-text">Date of Birth: {medicalRecord.dateOfBirth}</p>
      </div>

      {/* Allergies */}
      <div className="rec-section">
        <h2 className="rec-section-header">Allergies</h2>
        {medicalRecord.allergies.map((allergy, index) => (
          <p key={index} className="rec-info-text">- {allergy}</p>
        ))}
      </div>

      {/* Medical Conditions */}
      <div className="rec-section">
        <h2 className="rec-section-header">Medical Conditions</h2>
        {medicalRecord.medicalConditions.map((condition, conditionIndex) => (
          <div key={conditionIndex} className="rec-condition-container">
            <button
              className="rec-condition-button"
              onClick={() => toggleConditionExpand(conditionIndex)}
            >
              <p className="rec-condition-name">{condition.medCondition}</p>
            </button>
            {expandedConditionIndex === conditionIndex && (
              <div className="rec-condition-details">
                <p className="rec-info-text">Notes: {condition.notes}</p>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Medical Tests */}
      <div className="rec-section">
        <h2 className="rec-section-header">Medical Tests</h2>
        {medicalRecord.medicalTests.map((test, testIndex) => (
          <div key={testIndex} className="rec-test-container">
            <button
              className="rec-test-button"
              onClick={() => toggleTestExpand(testIndex)}
            >
              <p className="rec-test-type">{test.testType}</p>
              <p className="rec-test-subject">{test.subjectOfTest}</p>
            </button>
            {expandedTestIndex === testIndex && (
              <div className="rec-test-details">
                <p className="rec-info-text">Result: {test.result}</p>
                <p className="rec-info-text">Uploaded on: {test.dateTimeOfUpload}</p>
                <img src={test.imageOfScan} alt="Test Image" className="rec-test-image"/>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Prescriptions */}
      <div className="rec-section">
        <h2 className="rec-section-header">Prescriptions</h2>
        {medicalRecord.prescriptions.map((prescription, prescIndex) => (
          <div key={prescIndex} className="rec-prescription-container">
            <button
              className="rec-prescription-button"
              onClick={() => togglePrescriptionExpand(prescIndex, prescIndex)}
            >
              <p className="rec-doctor-name">Doctor: {prescription.doctorName}</p>
              <p className="rec-prescription-date">Date: {prescription.dateOfPrescription}</p>
            </button>
            {expandedPrescriptionIndex[prescIndex] === prescIndex && (
              <div className="rec-prescription-details">
                {prescription.medicines.map((medicine, medicineIndex) => (
                  <div key={medicineIndex}>
                    <p className="rec-medicine-name">{medicine.medicineName}</p>
                    <p className="rec-info-text">Form of Intake: {medicine.formOfIntake}</p>
                    <p className="rec-info-text">Subscription Heading: {medicine.subscriptionHeading}</p>
                    <p className="rec-info-text">Duration of Intake: {medicine.durationOfIntake} days</p>
                    <p className="rec-info-text">Frequency of Intake: {medicine.frequencyOfIntake}</p>
                    <p className="rec-info-text">Side Effects: {medicine.sideEffects}</p>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};


// App Component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginScreen />} />
        <Route path="/signup" element={<SignupScreen />} />
        <Route path="/home" element={<HomeScreen />} />
        <Route path="/doctor-selection" element={<DoctorSelectionScreen />} />
        <Route path="/doctor-details" element={<DoctorDetailsScreen />} />
        <Route path="/date-selection" element={<DateSelectionScreen />} />
        <Route path="/time-selection" element={<TimeSelectionScreen />} />
        <Route path="/confirmation" element={<ConfirmationScreen />} />
        <Route path="/manage-profile" element={<ManageProfileScreen />} />
        <Route path="/view-appointments" element={<ViewAppointmentsScreen />} />
        <Route path="/details" element={<DetailsScreen />} />
        <Route path="/cancel" element={<CancelScreen />} />
        <Route path="/review" element={<ReviewScreen />} />
        <Route path="/rebook" element={<RebookScreen />} />
        <Route path="/medical-records" element={<MedicalRecordsScreen />} />

 
      </Routes>
    </Router>
  );
}

export default App;