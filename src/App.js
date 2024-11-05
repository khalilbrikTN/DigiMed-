import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, Button, Image, Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import 'react-native-gesture-handler';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { Calendar } from 'react-native-calendars'; // Import calendar component
import { useNavigation } from '@react-navigation/native';
import FontAwesome from 'react-native-vector-icons/FontAwesome';

const Stack = createStackNavigator();




// Login Screen
function LoginScreen({ navigation }) {
  const [password, setPassword] = useState('');
  const [name, setUserName] = useState('');

  const handleLogin = () => {
    navigation.replace('Home', { userName: name });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to DigiMed!</Text>
      <Text style={styles.subtitle}>Login to your account.</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your user name"
        value={name}
        onChangeText={setUserName}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <TouchableOpacity style={styles.forgotPassword}>
        <Text style={styles.forgotPasswordText}>Forgot password?</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => navigation.navigate('Sign Up')}>
        <Text style={styles.signupText}>Don’t have an account? Sign up</Text>
      </TouchableOpacity>
    </View>
  );
}

// Signup Screen
function SignupScreen({ navigation }) {
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');

  const handleSignup = () => {
    navigation.replace('Home', { userName: name });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to DigiMed!</Text>
      <Text style={styles.subtitle}>Sign up to your account.</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your Name"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Phone Number"
        value={phone}
        onChangeText={setPhone}
        keyboardType="phone-pad"
      />
      <TextInput
        style={styles.input}
        placeholder="Create Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <TouchableOpacity style={styles.button} onPress={handleSignup}>
        <Text style={styles.buttonText}>Sign Up</Text>
      </TouchableOpacity>
    </View>
  );
}
// Function to handle logout
const handleLogout = (navigation) => {
  // Resetting the navigation stack and navigating to Login
  navigation.reset({
    index: 0,
    routes: [{ name: 'Login' }],
  });
};

// Home Screen
function HomeScreen({ route, navigation }) {
  const { userName } = route.params || {}; // Provide a default value for userName
  React.useLayoutEffect(() => {
    navigation.setOptions({
      headerRight: () => (
        <TouchableOpacity onPress={() => handleLogout(navigation)}>
          <Text style={{ color: 'blue', marginRight: 10 }}>Log Out</Text>
        </TouchableOpacity>
      ),
    });
  }, [navigation]);
  return (
    <View style={homeStyles.container}>
      <Text style={homeStyles.welcomeText}>Welcome Back {userName}</Text>
      <View style={homeStyles.buttonContainer}>
        <View style={homeStyles.row}>
          <TouchableOpacity style={homeStyles.button} onPress={() => navigation.navigate('Manage Profile')}>
            <Text>Manage Profile</Text>
          </TouchableOpacity>
          <TouchableOpacity style={homeStyles.button} onPress={() => navigation.navigate('View Appointments')}>
            <Text>View Appointments</Text>
          </TouchableOpacity>
        </View>
        <View style={homeStyles.row}>
          <TouchableOpacity style={homeStyles.button} onPress={() => navigation.navigate('Doctor Selection')}>
            <Text>Scheduling</Text>
          </TouchableOpacity>
          <TouchableOpacity style={homeStyles.button} onPress={() => navigation.navigate('Medical Records')}>
            <Text>Medical Records</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
}
// Doctors Data
const doctors = [
  {
    id: '1',
    name: 'Dr. Khalil',
    availableDates: ['2024-11-05', '2024-11-07', '2024-11-10'],
    rating: 4.5,
  },
  {
    id: '2',
    name: 'Dr. Yasmina',
    availableDates: ['2024-11-06', '2024-11-08', '2024-11-12'],
    rating: 3.5,
  },
  {
    id: '3',
    name: 'Dr. Rana',
    availableDates: ['2024-11-05', '2024-11-09', '2024-11-11'],
    rating: 5,
  },
];

function DoctorSelectionScreen({ navigation }) {
  const [selectedDoctor, setSelectedDoctor] = useState(null);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Select a Doctor</Text>
      {doctors.map(doctor => (
        <TouchableOpacity
          key={doctor.id}
          style={styles.doctorCard}
          onPress={() => navigation.navigate('Doctor Details', { doctor })}
        >
          <Image
            style={styles.doctorImage}
            source={require('./assets/download.png')}
          />
          <View style={styles.doctorInfo}>
            <Text style={styles.doctorName}>{doctor.name}</Text>
            <Text style={styles.specialty}>{doctor.specialty}</Text>
            <View style={styles.ratingContainer}>
              {Array.from({ length: 5 }).map((_, index) => (
                <FontAwesome
                  key={index}
                  name="star"
                  size={15}
                  color={index < Math.round(doctor.rating) ? '#FFD700' : '#ddd'}
                />
              ))}
            </View>
          </View>
        </TouchableOpacity>
      ))}
    </ScrollView>
  );
}

// Doctor Details Screen
function DoctorDetailsScreen({ route, navigation }) {
  const { doctor } = route.params;

  return (
    <View style={styles.detailsContainer}>
      <Image
        style={styles.largeDoctorImage}
        source={require('./assets/download.png')}
      />
      <Text style={styles.doctorName}>{doctor.name}</Text>
      <Text style={styles.specialty}>{doctor.specialty}</Text>
      <Text style={styles.experience}>{doctor.experience}</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('Date Selection', { doctor })}
      >
        <Text style={styles.buttonText}>Book Appointment</Text>
      </TouchableOpacity>
    </View>
  );
}

// Date Selection Screen
function DateSelectionScreen({ route, navigation }) {
  const { doctor } = route.params;
  const [selectedDate, setSelectedDate] = useState(null);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Select a Date with {doctor.name}</Text>
      <Calendar
        onDayPress={day => setSelectedDate(day.dateString)}
        markedDates={{
          [selectedDate]: { selected: true, marked: true },
        }}
      />
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('Time Selection', { doctor, selectedDate })}
      >
        <Text style={styles.buttonText}>Next</Text>
      </TouchableOpacity>
    </View>
  );
}

// Time Slot Selection Screen
function TimeSelectionScreen({ route, navigation }) {
  const { doctor, selectedDate } = route.params;
  const availableTimes = ['10:00 AM', '11:00 AM', '1:00 PM', '3:00 PM', '4:30 PM'];
  const [selectedTime, setSelectedTime] = useState(null);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Available Times on {selectedDate}</Text>
      {availableTimes.map(time => (
        <TouchableOpacity
          key={time}
          style={[
            styles.timeSlot,
            selectedTime === time && styles.selectedTimeSlot,
          ]}
          onPress={() => setSelectedTime(time)}
        >
          <Text style={styles.timeText}>{time}</Text>
        </TouchableOpacity>
      ))}
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('Confirmation', { doctor, selectedDate, selectedTime })}
      >
        <Text style={styles.buttonText}>Confirm Appointment</Text>
      </TouchableOpacity>
    </View>
  );
}

// Confirmation Screen
function ConfirmationScreen({ route, navigation }) {
  const { doctor, selectedDate, selectedTime } = route.params;

  const handleFinish = () => {
    Alert.alert('Success', 'Your appointment is confirmed!', [
      { text: 'OK', onPress: () => navigation.navigate('Home') }, // Adjust the name of your home screen if necessary
    ]);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Appointment Confirmation</Text>
      <Text style={styles.confirmationText}>Doctor: {doctor.name}</Text>
      <Text style={styles.confirmationText}>Specialty: {doctor.specialty}</Text>
      <Text style={styles.confirmationText}>Date: {selectedDate}</Text>
      <Text style={styles.confirmationText}>Time: {selectedTime}</Text>
      <TouchableOpacity style={styles.button} onPress={handleFinish}>
        <Text style={styles.buttonText}>Finish</Text>
      </TouchableOpacity>
    </View>
  );
}
// Manage Profile Screen
function ManageProfileScreen() {
  const [name, EditName] = useState('');
  const [phone, EditPhone] = useState('');
  const [Email, EditEmail] = useState('');
  const [Dob, EditDob] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Profile</Text>
      <Image
       source={require('./assets/download.png')}
        style={styles.profilePicture}
      />
      <TextInput
        style={styles.input}
        placeholder="Edit your Name"
        value={name}
        onChangeText={EditName}
      />
      <TextInput
        style={styles.input}
        placeholder="Edit your Phone Number"
        value={phone}
        onChangeText={EditPhone}
        keyboardType="phone-pad"
      />
      <TextInput
        style={styles.input}
        placeholder="Edit your Email"
        value={Email}
        onChangeText={EditEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Edit your Date of Birth"
        value={Dob}
        onChangeText={EditDob}
      />
      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Save Changes</Text>
      </TouchableOpacity>
    </View>
  );
}

// View Appointments Screen
const sampleAppointments = [
  { id: 1, doctor: 'Dr. Rana Taher', specialty: 'Dermatologist', date: 'Sunday, 2 June', time: '9:30 AM - 10:00 AM', status: 'Complete' },
  { id: 2, doctor: 'Dr. Youssef Farid', specialty: 'Oncologist', date: 'Sunday, 2 June', time: '9:30 AM - 10:00 AM', status: 'Complete' },
  { id: 3, doctor: 'Dr. Yasmina Mahdy', specialty: 'Psychiatrist', date: 'Sunday, 2 June', time: '9:30 AM - 10:00 AM', status: 'Complete' },
  { id: 4, doctor: 'Dr. Mostafa Youssef', specialty: 'Dermatologist', date: 'Sunday, 12 June', time: '9:30 AM - 10:00 AM', status: 'Upcoming' },
  { id: 5, doctor: 'Dr. Ahmed Fawzy', specialty: 'Oncologist', date: 'Sunday, 12 June', time: '9:30 AM - 10:00 AM', status: 'Upcoming' },
  { id: 6, doctor: 'Dr. Mohamed Khalil', specialty: 'Psychiatrist', date: 'Sunday, 12 June', time: '9:30 AM - 10:00 AM', status: 'Upcoming' },
  { id: 7, doctor: 'Dr. Sara El Said', specialty: 'Cardiologist', date: 'Sunday, 2 June', time: '9:30 AM - 10:00 AM', status: 'Cancelled' },
];
const DetailsScreen = ({ route, navigation }) => {
  const { appointment } = route.params; // Get appointment details passed as params

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 10 }}>Appointment Details</Text>
      <Text style={{ fontSize: 18 }}>Doctor: {appointment.doctor}</Text>
      <Text style={{ fontSize: 18 }}>Specialty: {appointment.specialty}</Text>
      <Text style={{ fontSize: 18 }}>Date: {appointment.date}</Text>
      <Text style={{ fontSize: 18 }}>Time: {appointment.time}</Text>
      <Text style={{ fontSize: 18 }}>Location: {appointment.location}</Text>
      <Text style={{ fontSize: 18, marginTop: 10 }}>Notes: {appointment.notes || 'No additional notes'}</Text>

      <Button title="Back to Appointments" onPress={() => navigation.goBack()} />
    </View>
  );
};
const CancelScreen = ({ route, navigation }) => {
  const { appointmentId } = route.params;

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text>Cancel Appointment for ID: {appointmentId}</Text>
      <TextInput placeholder="Enter reason for cancellation" style={{ marginVertical: 20, borderWidth: 1, padding: 8 }} />
      <Button title="Confirm Cancellation" onPress={() => navigation.goBack()} />
    </View>
  );
};
const ReviewScreen = ({ route, navigation }) => {
  const { appointmentId } = route.params;

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text>Add Review for Appointment ID: {appointmentId}</Text>
      <TextInput placeholder="Write your review here" style={{ marginVertical: 20, borderWidth: 1, padding: 8 }} />
      <Button title="Submit Review" onPress={() => navigation.goBack()} />
    </View>
  );
};
const RebookScreen = ({ route, navigation }) => {
  const { appointmentId } = route.params;

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Rebook Appointment for ID: {appointmentId}</Text>
      {/* Implement your rebook functionality here */}
      <Button title="Confirm Rebook" onPress={() => navigation.goBack()} />
    </View>
  );
};

function ViewAppointmentsScreen() {
  const navigation = useNavigation();

  const [selectedTab, setSelectedTab] = useState('Upcoming');

  // Filter appointments based on selected tab
  const filteredAppointments = sampleAppointments.filter(appointment => appointment.status === selectedTab);

  return (
    <View style={styles.viewappointment_mainContainer}>
      {/* Header */}
      <Text style={styles.viewappointment_heading}>All Appointments</Text>

      {/* Tabs */}
      <View style={styles.viewappointment_tabs}>
        <TouchableOpacity onPress={() => setSelectedTab('Complete')} style={[styles.viewappointment_tabButton, selectedTab === 'Complete' && styles.viewappointment_tabButtonActive]}>
          <Text style={styles.viewappointment_tabText}>Complete</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => setSelectedTab('Upcoming')} style={[styles.viewappointment_tabButton, selectedTab === 'Upcoming' && styles.viewappointment_tabButtonActive]}>
          <Text style={styles.viewappointment_tabText}>Upcoming</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => setSelectedTab('Cancelled')} style={[styles.viewappointment_tabButton, selectedTab === 'Cancelled' && styles.viewappointment_tabButtonActive]}>
          <Text style={styles.viewappointment_tabText}>Cancelled</Text>
        </TouchableOpacity>
      </View>

      {/* Appointment List */}
      <ScrollView contentContainerStyle={styles.viewappointment_scrollContainer}>
        {filteredAppointments.map((appointment) => (
          <View key={appointment.id} style={styles.viewappointment_cardContainer}>
            <View style={styles.viewappointment_doctorInfo}>
              <Text style={styles.viewappointment_doctorName}>{appointment.doctor}</Text>
              <Text style={styles.viewappointment_specialty}>{appointment.specialty}</Text>
              <Text style={styles.viewappointment_date}>{appointment.date}</Text>
              <Text style={styles.viewappointment_time}>{appointment.time}</Text>
            </View>

            {/* Action Buttons Based on Tab */}
            {selectedTab === 'Upcoming' && (
              <View style={styles.viewappointment_buttonContainer}>
                <TouchableOpacity
                  style={styles.viewappointment_detailsButton}
                  onPress={() => navigation.navigate('Details', { appointment })}
                >
                  <Text style={styles.viewappointment_buttonText}>Details</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={styles.viewappointment_cancelButton}
                  onPress={() => navigation.navigate('Cancel', { appointmentId: appointment.id })}
                >
                  <Text style={styles.viewappointment_buttonText}>X</Text>
                </TouchableOpacity>
              </View>
            )}
            {selectedTab === 'Complete' && (
              <View style={styles.viewappointment_buttonContainer}>
                <TouchableOpacity
                  style={styles.viewappointment_rebookButton}
                  onPress={() => navigation.navigate('Doctor Selection', { appointmentId: appointment.id })}
                >
                  <Text style={styles.viewappointment_buttonText}>Re-Book</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={styles.viewappointment_addReviewButton}
                  onPress={() => navigation.navigate('Review', { appointmentId: appointment.id })}
                >
                  <Text style={styles.viewappointment_buttonText}>Add Review</Text>
                </TouchableOpacity>
              </View>
            )}
            {selectedTab === 'Cancelled' && (
              <View style={styles.viewappointment_buttonContainer}>
                <TouchableOpacity
                  style={styles.viewappointment_addReviewButton}
                  onPress={() => navigation.navigate('Review', { appointmentId: appointment.id })}
                >
                  <Text style={styles.viewappointment_buttonText}>Add Review</Text>
                </TouchableOpacity>
              </View>
            )}
          </View>
        ))}
      </ScrollView>
    </View>
  );
}


// Medical Records Screen
const medicalRecord = {
  patientName: 'Omar Omar',
  dateOfBirth: '2005-05-25',
  allergies: ['Peanuts', 'Carrots'],
  visits: [
    {
      date: '2024-10-15',
      doctorName: 'Dr. Ali Ahmed',
      diagnosis: 'Hypertension',
      prescriptions: [
        {
          medicineName: 'Panadol',
          dosage: '10 mg',
          frequency: 'Once daily',
          duration: '30 days',
          sideEffects: 'Headache, Muscle pain',
        },
      ],
    },
    {
      date: '2024-11-01',
      doctorName: 'Dr. Laila Hassan',
      diagnosis: 'Diabetes',
      prescriptions: [
        {
          medicineName: 'Metformin',
          dosage: '500 mg',
          frequency: 'Twice daily',
          duration: '60 days',
          sideEffects: 'Nausea, Diarrhea',
        },
      ],
    },
    {
      date: '2024-11-01',
      doctorName: 'Dr. Salma Swelam',
      diagnosis: 'Flu',
      prescriptions: [
        {
          medicineName: 'Augmentin',
          dosage: '500 mg',
          frequency: 'Twice daily',
          duration: '60 days',
          sideEffects: 'Nausea, Diarrhea',
        },
      ],
    },
  ],
};

const MedicalRecordsScreen = () => {
  const [expandedVisitIndex, setExpandedVisitIndex] = useState(null);
  const [expandedPrescriptionIndex, setExpandedPrescriptionIndex] = useState({});

  const toggleVisitExpand = (index) => {
    setExpandedVisitIndex(expandedVisitIndex === index ? null : index);
  };

  const togglePrescriptionExpand = (visitIndex, prescIndex) => {
    setExpandedPrescriptionIndex((prevState) => ({
      ...prevState,
      [visitIndex]: prevState[visitIndex] === prescIndex ? null : prescIndex,
    }));
  };

  return (
    <ScrollView style={styles.rec_container} contentContainerStyle={styles.rec_contentContainer}>
      {/* Header Section */}
      <View style={styles.rec_header}>
        <Text style={styles.rec_headerText}>Medical Record</Text>
      </View>

      {/* Patient Info */}
      <View style={styles.rec_section}>
        <Text style={styles.rec_sectionHeader}>Patient Information</Text>
        <Text style={styles.rec_infoText}>Name: {medicalRecord.patientName}</Text>
        <Text style={styles.rec_infoText}>Date of Birth: {medicalRecord.dateOfBirth}</Text>
      </View>

      {/* Allergies */}
      <View style={styles.rec_section}>
        <Text style={styles.rec_sectionHeader}>Allergies</Text>
        {medicalRecord.allergies.map((allergy, index) => (
          <Text key={index} style={styles.rec_infoText}>- {allergy}</Text>
        ))}
      </View>

      {/* Visits */}
      <View style={styles.rec_section}>
        <Text style={styles.rec_sectionHeader}>Doctor Visits</Text>
        {medicalRecord.visits.map((visit, visitIndex) => (
          <View key={visitIndex} style={styles.rec_visitContainer}>
            <TouchableOpacity onPress={() => toggleVisitExpand(visitIndex)}>
              <Text style={styles.rec_visitDate}>Visit Date: {visit.date}</Text>
              <Text style={styles.rec_doctorName}>Doctor: {visit.doctorName}</Text>
            </TouchableOpacity>
            {expandedVisitIndex === visitIndex && (
              <View style={styles.rec_visitDetails}>
                <Text style={styles.rec_infoText}>Diagnosis: {visit.diagnosis}</Text>

                {/* Prescriptions for the visit */}
                <Text style={styles.rec_sectionSubHeader}>Prescriptions:</Text>
                {visit.prescriptions.map((prescription, prescIndex) => (
                  <View key={prescIndex} style={styles.rec_prescriptionContainer}>
                    <TouchableOpacity onPress={() => togglePrescriptionExpand(visitIndex, prescIndex)}>
                      <Text style={styles.rec_medicineName}>{prescription.medicineName}</Text>
                    </TouchableOpacity>
                    {expandedPrescriptionIndex[visitIndex] === prescIndex && (
                      <View style={styles.rec_prescriptionDetails}>
                        <Text style={styles.rec_infoText}>Dosage: {prescription.dosage}</Text>
                        <Text style={styles.rec_infoText}>Frequency: {prescription.frequency}</Text>
                        <Text style={styles.rec_infoText}>Duration: {prescription.duration}</Text>
                        <Text style={styles.rec_infoText}>Side Effects: {prescription.sideEffects}</Text>
                      </View>
                    )}
                  </View>
                ))}
              </View>
            )}
          </View>
        ))}
      </View>
    </ScrollView>
  );
};

// Main App Component
export default function App() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="Sign Up" component={SignupScreen} />
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="Manage Profile" component={ManageProfileScreen} />
          <Stack.Screen name="View Appointments" component={ViewAppointmentsScreen} />
          <Stack.Screen name="Medical Records" component={MedicalRecordsScreen} />
          <Stack.Screen name="Rebook" component={RebookScreen} />
          <Stack.Screen name="Review" component={ReviewScreen} />
          <Stack.Screen name="Cancel" component={CancelScreen} />
          <Stack.Screen name="Details" component={DetailsScreen} />
          <Stack.Screen name="Doctor Selection" component={DoctorSelectionScreen} />
        <Stack.Screen name="Doctor Details" component={DoctorDetailsScreen} />
        <Stack.Screen name="Date Selection" component={DateSelectionScreen} />
        <Stack.Screen name="Time Selection" component={TimeSelectionScreen} />
        <Stack.Screen name="Confirmation" component={ConfirmationScreen} />
        </Stack.Navigator>
      </NavigationContainer>
    </GestureHandlerRootView>
  );
}

// Styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
    backgroundColor: '#f9f9f9',
    flex: 1,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',

  },
  subtitle: {
    fontSize: 18,
    marginVertical: 10,
    textAlign: 'center',

  },
  input: {
    width: '100%',
    height: 50,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 5,
    paddingHorizontal: 10,
    marginBottom: 10,
  },
  button: {
    backgroundColor: '#007bff',
    padding: 15,
    borderRadius: 5,
    marginVertical: 10,
    width: '100%',
  },
  buttonText: {
    color: '#fff',
    textAlign: 'center',
    fontWeight: 'bold',
  },
  forgotPassword: {
    alignSelf: 'flex-end',
    marginBottom: 20,
  },
  forgotPasswordText: {
    color: '#007bff',
    fontSize: 14,
  },
  signupText: {
    color: '#007bff',
    marginTop: 10,
    textAlign: 'center',
  },
  doctorCard: {
    padding: 10,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    marginVertical: 5,
    width: '100%',
  },
  selectedDoctor: {
    backgroundColor: '#d1e7dd',
  },
  doctorName: {
    fontSize: 18,
  },
  appointmentCard: {
    padding: 10,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    marginVertical: 5,
  },
  profilePicture: {
    width: 100,
    height: 100,
    borderRadius: 50,
    marginBottom: 10,
  },
  navButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginTop: 20,
  },
  navButton: {
    padding: 10,
    backgroundColor: '#007bff',
    borderRadius: 5,
    width: '40%',
    alignItems: 'center',
  },
  mainContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'flex-start',
    padding: 16,
    backgroundColor: '#f9f9f9',
  },
  heading: {
    
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  scrollContainer: {
    flexGrow: 1,
    paddingVertical: 10,
    width: '100%',
  },
  cardContainer: {
    backgroundColor: '#fff',
    padding: 15,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    marginVertical: 10,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 3, // For Android shadow
  },
  cardText: {
    fontSize: 16,
    marginBottom: 5,
  },container: {
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginBottom: 20,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#007bff',

  },
  section: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginBottom: 15,
  },
  sectionHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
    paddingBottom: 5,
    color: '#007bff',

  },
  infoText: {
    fontSize: 16,
    marginBottom: 5,

  },
  visitContainer: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    borderRadius: 5,
    marginBottom: 10,
    backgroundColor: '#fff',
  },
  visitDate: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  doctorName: {
    fontSize: 16,
    color: '#555',
    marginBottom: 5,
  },
  visitDetails: {
    marginTop: 10,
  },
  sectionSubHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: 10,
  },
  prescriptionContainer: {
    marginTop: 5,
    padding: 10,
    backgroundColor: '#f0f0f0',
    borderRadius: 5,
  },
  medicineName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#007bff',

  },
  prescriptionDetails: {
    marginTop: 5,
  },
  viewappointment_mainContainer: {
    flex: 1,
    backgroundColor: '#F5F6FA',
    paddingHorizontal: 20,
  },
  viewappointment_heading: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 20,
    marginBottom: 10,
    color: '#333',
  },
  viewappointment_tabs: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginVertical: 15,
  },
  viewappointment_tabButton: {
    paddingVertical: 10,
    paddingHorizontal: 15,
    borderRadius: 20,
    backgroundColor: '#E6E8F0',
  },
  viewappointment_tabButtonActive: {
    backgroundColor: '#0066FF',
  },
  viewappointment_tabText: {
    color: '#333',
    fontWeight: 'bold',
  },
  viewappointment_scrollContainer: {
    paddingBottom: 20,
  },
  viewappointment_cardContainer: {
    backgroundColor: '#EEF3FF',
    borderRadius: 15,
    padding: 15,
    marginBottom: 15,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  viewappointment_doctorInfo: {
    flex: 1,
  },
  viewappointment_doctorName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  viewappointment_specialty: {
    fontSize: 14,
    color: '#555',
  },
  viewappointment_date: {
    fontSize: 13,
    color: '#777',
    marginTop: 5,
  },
  viewappointment_time: {
    fontSize: 13,
    color: '#777',
  },
  viewappointment_buttonContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  viewappointment_detailsButton: {
    backgroundColor: '#0066FF',
    paddingVertical: 5,
    paddingHorizontal: 15,
    borderRadius: 10,
    marginRight: 5,
  },
  viewappointment_cancelButton: {
    backgroundColor: '#FF5C5C',
    paddingVertical: 5,
    paddingHorizontal: 10,
    borderRadius: 10,
  },
  viewappointment_rebookButton: {
    backgroundColor: '#4CAF50',
    paddingVertical: 5,
    paddingHorizontal: 15,
    borderRadius: 10,
    marginRight: 5,
  },
  viewappointment_addReviewButton: {
    backgroundColor: '#0066FF',
    paddingVertical: 5,
    paddingHorizontal: 15,
    borderRadius: 10,
  },
  viewappointment_buttonText: {
    color: '#FFFFFF',
    fontSize: 13,
  },
  viewappointment_rebookButton: {
    backgroundColor: '#4CAF50',
    padding: 8,
    borderRadius: 4,
    marginTop: 8,
    alignItems: 'center',
  },
  viewappointment_reviewButton: {
    backgroundColor: '#2196F3',
    padding: 8,
    borderRadius: 4,
    marginTop: 8,
    alignItems: 'center',
  },
  viewappointment_cancelButton: {
    backgroundColor: '#f44336',
    padding: 8,
    borderRadius: 4,
    marginTop: 8,
    alignItems: 'center',
  },
  viewappointment_buttonText: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  viewappointment_detailsButton: {
    backgroundColor: '#007bff',
    padding: 8,
    borderRadius: 4,
    marginTop: 8,
    alignItems: 'center',
  },
  container: { flex: 1, padding: 16, backgroundColor: '#fff' },
 
  doctorCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#f9f9f9',
    padding: 10,
    marginVertical: 8,
    borderRadius: 10,
  },
  doctorImage: { width: 50, height: 50, borderRadius: 25, marginRight: 10 },
  doctorInfo: { flex: 1 },
  doctorName: { fontSize: 18, fontWeight: 'bold' },
  specialty: { fontSize: 14, color: '#555' },
  ratingContainer: { flexDirection: 'row', marginTop: 4 },
  largeDoctorImage: { width: 100, height: 100, borderRadius: 50, marginBottom: 10 },
  detailsContainer: { flex: 1, alignItems: 'center', padding: 20 },
  experience: { fontSize: 14, color: '#888', marginBottom: 20 },
  button: {
    backgroundColor: '#007BFF',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
   
  },
  buttonText: { color: '#fff', fontSize: 16, fontWeight: 'bold' },
  timeSlot: {
    padding: 15,
    backgroundColor: '#f0f0f0',
    marginVertical: 5,
    borderRadius: 8,
    alignItems: 'center',
  },
  selectedTimeSlot: { backgroundColor: '#007BFF' },
  timeText: { color: '#333' },
  confirmationText: { fontSize: 16, marginVertical: 4 },
  rec_container: {
    flex: 1,
    backgroundColor: '#f5f5f5', // Light background color
  },
  rec_contentContainer: {
    padding: 16,
  },
  rec_header: {
    paddingVertical: 20,
    alignItems: 'center',
    backgroundColor: '#4a90e2', // Header background color
    borderRadius: 10,
    marginBottom: 16,
  },
  rec_headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ffffff', // Header text color
  },
  rec_section: {
    marginVertical: 12,
    backgroundColor: '#ffffff', // Section background color
    padding: 10,
    borderRadius: 8,
    elevation: 2, // Shadow for Android
    shadowColor: '#000', // Shadow for iOS
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.2,
    shadowRadius: 1,
  },
  rec_sectionHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333', // Section header text color
  },
  rec_infoText: {
    fontSize: 16,
    marginVertical: 4,
    color: '#666', // Info text color
  },
  rec_visitContainer: {
    marginBottom: 10,
  },
  rec_visitButton: {
    padding: 10,
    backgroundColor: '#e8f0fe', // Visit button background color
    borderRadius: 5,
  },
  rec_visitDate: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1a73e8', // Visit date text color
  },
  rec_doctorName: {
    fontSize: 16,
    color: '#555', // Doctor name text color
  },
  rec_visitDetails: {
    paddingLeft: 10,
    marginTop: 5,
  },
  rec_prescriptionContainer: {
    marginTop: 5,
  },
  rec_prescriptionButton: {
    padding: 5,
    backgroundColor: '#f0f4ff', // Prescription button background color
    borderRadius: 5,
  },
  rec_medicineName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1a73e8', // Medicine name text color
  },
  rec_prescriptionDetails: {
    paddingLeft: 10,
    marginTop: 5,
  },
  rec_sectionSubHeader: {
    fontSize: 16,
    fontWeight: '600',
    marginTop: 8,
    color: '#333', // Subheader color
  },
});

// Home Screen Styles
const homeStyles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#f9f9f9',
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  buttonContainer: {
    width: '100%',
    alignItems: 'center',
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 10, 
  },
  button: {
    backgroundColor: '#007bff',
    padding: 15,
    borderRadius: 5,
    width: '45%', 
  },

});


