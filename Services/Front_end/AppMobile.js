import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ScrollView, Button, Image, FlatList,Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import 'react-native-gesture-handler';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { Calendar } from 'react-native-calendars'; // Import calendar component
import { useNavigation } from '@react-navigation/native';
import FontAwesome from 'react-native-vector-icons/FontAwesome';
import DropDownPicker from 'react-native-dropdown-picker';

const Stack = createStackNavigator();


const medicalRecord = {
  patientName: "Hoda",
  dateOfBirth: "2005-03-25",
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
const sampleAppointments = [
  { id: 1, doctor: { name: "Dr. Rana Taher", specialty: "Dermatologist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Complete" },
  { id: 2, doctor: { name: "Dr. Youssef Farid", specialty: "Oncologist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Complete" },
  { id: 3, doctor: { name: "Dr. Yasmina Mahdy", specialty: "Psychiatrist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Complete" },
  { id: 4, doctor: { name: "Dr. Mostafa Youssef", specialty: "Dermatologist" }, date: "Sunday, 12 June", time: "9:30 AM - 10:00 AM", status: "Upcoming" },
  { id: 5, doctor: { name: "Dr. Ahmed Fawzy", specialty: "Oncologist" }, date: "Sunday, 12 June", time: "9:30 AM - 10:00 AM", status: "Upcoming" },
  { id: 6, doctor: { name: "Dr. Mohamed Khalil", specialty: "Psychiatrist" }, date: "Sunday, 12 June", time: "9:30 AM - 10:00 AM", status: "Upcoming" },
  { id: 7, doctor: { name: "Dr. Sara El Said", specialty: "Cardiologist" }, date: "Sunday, 2 June", time: "9:30 AM - 10:00 AM", status: "Cancelled" },
];

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
const SignupScreen = ({ navigation }) => {
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
  const [open, setOpen] = useState(false);
  const [items, setItems] = useState([
    { label: 'Male', value: 'M' },
    { label: 'Female', value: 'F' },
    { label: 'Other', value: 'O' },
  ]);

  const handleSignup = () => {
    navigation.replace('Home', { userName: firstName });
  
    // Navigate to Profile screen after successful signup
    navigation.replace('Manage Profile', { 
      firstName, 
      middleName, 
      lastName, 
      phoneNumber, 
      email, 
      dob,
      street,
      region,
      city,
      gender,
      bloodType,
      height,
      weight,
    });
    navigation.navigate('Home',{firstName});
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Welcome to DigiMed!</Text>
      <Text style={styles.subtitle}>Sign up to your account.</Text>
      
      <TextInput
        style={styles.input}
        placeholder="Enter your First Name"
        value={firstName}
        onChangeText={setFirstName}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Middle Name"
        value={middleName}
        onChangeText={setMiddleName}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Last Name"
        value={lastName}
        onChangeText={setLastName}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Phone Number"
        value={phoneNumber}
        onChangeText={setPhoneNumber}
        keyboardType="phone-pad"
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Email Address"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Date of Birth"
        value={dob}
        onChangeText={setDob}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Street Address"
        value={street}
        onChangeText={setStreet}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Region"
        value={region}
        onChangeText={setRegion}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your City"
        value={city}
        onChangeText={setCity}
      />
      
      <DropDownPicker
        open={open}
        value={gender}
        items={items}
        setOpen={setOpen}
        setValue={setGender}
        setItems={setItems}
        placeholder="Select Gender"
        style={styles.dropdown}
        dropDownContainerStyle={styles.dropdownContainer}
      />

      <TextInput
        style={styles.input}
        placeholder="Enter your Blood Type"
        value={bloodType}
        onChangeText={setBloodType}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Height (cm)"
        value={height}
        onChangeText={setHeight}
        keyboardType="numeric"
      />
      <TextInput
        style={styles.input}
        placeholder="Enter your Weight (kg)"
        value={weight}
        onChangeText={setWeight}
        keyboardType="numeric"
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
    </ScrollView>
  );
};

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

  const { userName } = route.params || 'User';

  const upcomingAppointments = sampleAppointments.filter(
    (appointment) => appointment.status === 'Upcoming'
  );

  const medicationReminders = medicalRecord.prescriptions.flatMap((prescription) =>
    prescription.medicines.map((medicine) => ({
      name: medicine.medicineName,
      frequency: medicine.frequencyOfIntake,
      duration: medicine.durationOfIntake,
    }))
  );


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
    <ScrollView contentContainerStyle={homeStyles.container}>
      {/* Welcome Text */}
      <Text style={homeStyles.welcomeText}>Welcome Back{'\n'}{userName}</Text>

      {/* Upper Section */}
      <View style={homeStyles.upperSection}>
        {/* Profile Icon */}
        <View style={homeStyles.profileIconContainer}>
          <Image source={require('./assets/download.png')} style={homeStyles.profileIcon} />
        </View>

        {/* Manage Profile and View Appointments Buttons */}
        <View style={homeStyles.upperButtonsColumn}>
          <TouchableOpacity style={homeStyles.widgetButton} onPress={() => navigation.navigate('Manage Profile')}>
            <Text style={homeStyles.widgetText}>Manage Profile</Text>
          </TouchableOpacity>
          <TouchableOpacity style={homeStyles.widgetButton} onPress={() => navigation.navigate('View Appointments')}>
            <Text style={homeStyles.widgetText}>View Appointments</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* Lower Section */}
      <View style={homeStyles.lowerSection}>
        <View style={homeStyles.lowerButtonsRow}>
          <TouchableOpacity style={homeStyles.lowerWidgetButton} onPress={() => navigation.navigate('Doctor Selection',{userName})}>
            <Text style={homeStyles.lowerWidgetText}>Scheduling</Text>
          </TouchableOpacity>
          <TouchableOpacity style={homeStyles.lowerWidgetButton} onPress={() => navigation.navigate('Medical Records')}>
            <Text style={homeStyles.lowerWidgetText}>Medical Records</Text>
          </TouchableOpacity>
        </View>

        <View style={homeStyles.lowerButtonsRow}>
          <View style={homeStyles.infoWidgetButton}>
            <Text style={homeStyles.infoWidgetText}>Upcoming Appointments</Text>
            {upcomingAppointments.length > 0 ? (
          <FlatList
            data={upcomingAppointments}
            keyExtractor={(item) => item.id.toString()}
            renderItem={({ item }) => (
              <View style={homeStyles.infoWidget}>
                <Text style={homeStyles.subtitle}>Date: {item.date}</Text>
                <Text style={homeStyles.subtitle}>Time: {item.time}</Text>
                <Text style={homeStyles.subtitle}>Doctor: {item.doctor.name}</Text>
              </View>
            )}
          />
        ) : (
          <Text>No upcoming appointments.</Text>
        )}
          </View>
          <View style={homeStyles.infoWidgetButton} >
            <Text style={homeStyles.infoWidgetText}>Medication Reminders</Text>
            {medicationReminders.length > 0 ? (
          <FlatList
            data={medicationReminders}
            keyExtractor={(item, index) => index.toString()}
            renderItem={({ item }) => (
              <View style={homeStyles.infoWidget}>
                <Text style={homeStyles.subtitle}>Medicine: {item.name}</Text>
                <Text style={homeStyles.subtitle}>
                  Frequency: {item.frequency} for {item.duration} days
                </Text>
              </View>
            )}
          />
        ) : (
          <Text>No medication reminders.</Text>
        )}
          </View>
        </View>
      </View>
    </ScrollView>
  );
}
// Doctors Data
function DoctorSelectionScreen({ navigation,route}) {
  const [selectedDoctor, setSelectedDoctor] = useState(null);
  const { userName } = route.params || 'User';
  
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
  return (
    <ScrollView contentContainerStyle={doctorselection_styles.doctorselection_container}>
      <View style={doctorselection_styles.doctorselection_header}>
        <View>
          <Text style={doctorselection_styles.doctorselection_title}>Welcome Back</Text>
          <Text style={doctorselection_styles.doctorselection_username}>{ userName }</Text>
        </View>
        <FontAwesome name="user-circle" size={40} color="#1E88E5" />
      </View>

      {/* Search bar and favorites section */}
      <View style={doctorselection_styles.doctorselection_searchContainer}>
        <Text style={doctorselection_styles.doctorselection_tab}>Doctors</Text>
        <Text style={doctorselection_styles.doctorselection_tab}>Favorites</Text>
        <View style={doctorselection_styles.doctorselection_searchBar}>
          <FontAwesome name="search" size={20} color="#1E88E5" />
          <TextInput placeholder="Search..." style={doctorselection_styles.doctorselection_searchInput} />
        </View>
      </View>

      {/* Date and Time Container */}
      <View style={doctorselection_styles.doctorselection_dateTimeContainer}>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={doctorselection_styles.doctorselection_dateSelector}>
          {['19 MON', '20 TUE', '21 WED', '22 THU', '23 FRI', '24 SAT','25 SUN'].map((date, index) => (
            <View key={index} style={doctorselection_styles.doctorselection_dateWidget}>
              <Text style={doctorselection_styles.doctorselection_dateText}>{date.split(' ')[0]}</Text>
              <Text style={doctorselection_styles.doctorselection_dayText}>{date.split(' ')[1]}</Text>
            </View>
          ))}
        </ScrollView>

        {/* Time slots */}
        <View style={doctorselection_styles.doctorselection_timeSlots}>
          {['9 AM', '10 AM', '11 AM', '12 AM'].map((time, index) => (
            <View key={index} style={doctorselection_styles.doctorselection_timeWidget}>
              <Text style={doctorselection_styles.doctorselection_timeText}>{time}</Text>
              <Text style={doctorselection_styles.doctorselection_timeLine}>--------------------</Text>
            </View>
          ))}
        </View>
      </View>

      {/* Doctor cards */}
      {doctors.map(doctor => (
        <TouchableOpacity
          key={doctor.id}
          style={doctorselection_styles.doctorselection_doctorCard}
          onPress={() => navigation.navigate('Doctor Details', { doctor })}
        >
          <Image
            style={doctorselection_styles.doctorselection_doctorImage}
            source={require('./assets/download.png')}
          />
          <View style={doctorselection_styles.doctorselection_doctorInfo}>
            <Text style={doctorselection_styles.doctorselection_doctorName}>{doctor.first_name} {doctor.middle_name} {doctor.last_name}</Text>
            <Text style={doctorselection_styles.doctorselection_specialty}>{doctor.specialty}- {doctor.sub_specialty}</Text>
            <View style={doctorselection_styles.doctorselection_ratingContainer}>

            </View>
          </View>
          <FontAwesome name="info-circle" size={24} color="#1E88E5" style={doctorselection_styles.doctorselection_infoIcon} />
        </TouchableOpacity>
      ))}
    </ScrollView>
  );
}

const doctorselection_styles = {
  doctorselection_container: {
    flexGrow: 1,
    backgroundColor: 'white',
    padding: 20,
  },
  doctorselection_header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 20,
  },
  doctorselection_title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1E88E5',
  },
  doctorselection_username: {
    fontSize: 18,
    color: '#555',
  },
  doctorselection_searchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
    justifyContent: 'space-between',
  },
  doctorselection_tab: {
    fontSize: 16,
    color: '#1E88E5',
    fontWeight: 'bold',
  },
  doctorselection_searchBar: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#E3F2FD',
    borderRadius: 20,
    paddingHorizontal: 10,
    width: '60%',
  },
  doctorselection_searchInput: {
    flex: 1,
    marginLeft: 10,
  },
  doctorselection_dateTimeContainer: {
    backgroundColor: '#1E88E5',
    borderRadius: 15,
    padding: 15,
    marginBottom: 20,
    alignItems: 'center',

  },
  doctorselection_dateSelector: {
    flexDirection: 'row',
    marginBottom: 10,
    
  },
  doctorselection_dateWidget: {
    backgroundColor: '#FFFFFF',
    borderRadius: 10,
    paddingVertical: 8,
    paddingHorizontal: 10,
    marginRight: 10,
    alignItems: 'center',
  },
  doctorselection_dateText: {
    color: '#000000',
    fontSize: 16,
    fontWeight: 'bold',
  },
  doctorselection_dayText: {
    color: '#000000',
    fontSize: 14,
  },
  doctorselection_timeSlots: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  doctorselection_timeWidget: {
    backgroundColor: '#FFFFFF',
    padding: 8,
    borderRadius: 10,
    alignItems: 'center',
    marginHorizontal: 5,
  },
  doctorselection_timeText: {
    color: '#1E88E5',
    fontSize: 16,
    fontWeight: 'bold',
  },
  doctorselection_timeLine: {
    color: '#1E88E5',
  },
  doctorselection_doctorCard: {
    flexDirection: 'row',
    padding: 15,
    borderRadius: 10,
    backgroundColor: '#E3F2FD',
    marginBottom: 10,
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  doctorselection_doctorImage: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: '#E0E0E0',
    marginRight: 15,
  },
  doctorselection_doctorInfo: {
    flex: 1,
  },
  doctorselection_doctorName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1E88E5',
  },
  doctorselection_specialty: {
    fontSize: 14,
    color: '#777',
  },
  doctorselection_ratingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 5,
  },
  doctorselection_reviews: {
    color: '#777',
    marginLeft: 5,
  },
  doctorselection_infoIcon: {
    marginLeft: 10,
  },
};
// Doctor Details Screen
function DoctorDetailsScreen({ route, navigation }) {
  const { doctor } = route.params;

  return (
    <View style={styles.detailsContainer}>
      <Image
        style={styles.largeDoctorImage}
        source={require('./assets/download.png')}
      />
      <Text style={styles.doctorName}>{doctor.first_name} {doctor.middle_name} {doctor.last_name}</Text>
      <Text style={styles.specialty}>{doctor.specialty}</Text>
      <Text style={styles.experience}>{doctor.sub_specialty}</Text>
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
      <Text style={styles.title}>Select a Date with Dr. {doctor.first_name} {doctor.middle_name} {doctor.last_name}</Text>
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
      <Text style={styles.confirmationText}>Doctor: {doctor.first_name} {doctor.middle_name} {doctor.last_name}</Text>
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
function ManageProfileScreen({ route, navigation }) {
  const { 
    firstName = '', 
    middleName = '', 
    lastName = '', 
    phoneNumber = '', 
    email = '', 
    dob = '',
    street = '',
    region = '',
    city = '',
    gender = '',
    bloodType = '',
    height = '',
    weight = ''
  } = route.params || {}; 

  // Set up state for editable fields
  const [name, EditName] = useState(firstName || ''); 
  const [phone, EditPhone] = useState(phoneNumber || '');
  const [Email, EditEmail] = useState(email || '');
  const [Dob, EditDob] = useState(dob || '');
  const [BloodType, EditBloodType] = useState(bloodType || '');
  const [Height, EditHeight] = useState(height || '');
  const [Weight, EditWeight] = useState(weight || '');

  const handleSaveChanges = () => {
    // Handle the logic for saving changes (e.g., make an API call)
    Alert.alert('Profile updated successfully!');
   navigation.navigate('Home',{name})
  };

  return (
    <ScrollView style={styles.container}>
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
      <TextInput
        style={styles.input}
        placeholder="Edit your Blood Type"
        value={BloodType}
        onChangeText={EditBloodType}
      />
      <TextInput
        style={styles.input}
        placeholder="Edit your Height (cm)"
        value={Height}
        onChangeText={EditHeight}
        keyboardType="numeric"
      />
      <TextInput
        style={styles.input}
        placeholder="Edit your Weight (kg)"
        value={Weight}
        onChangeText={EditWeight}
        keyboardType="numeric"
      />
      <TouchableOpacity style={styles.button} onPress={handleSaveChanges}>
        <Text style={styles.buttonText}>Save Changes</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}


const DetailsScreen = ({ route, navigation }) => {
  const { appointment } = route.params; // Get appointment details passed as params

  return (
<View style={styles.detailsContainer}>
      <Text style={styles.headerText}>Appointment Details</Text>
      <View style={styles.detailsContent}>
        <Text style={styles.detailsText}><Text style={styles.boldText}>Doctor:</Text> {appointment.doctor?.name}</Text>
        <Text style={styles.detailsText}><Text style={styles.boldText}>Specialty:</Text> {appointment.doctor?.specialty}</Text>
        <Text style={styles.detailsText}><Text style={styles.boldText}>Date:</Text> {appointment.date}</Text>
        <Text style={styles.detailsText}><Text style={styles.boldText}>Time:</Text> {appointment.time}</Text>
        <Text style={styles.detailsText}><Text style={styles.boldText}>Location:</Text> {appointment.location || 'Not specified'}</Text>
        <Text style={styles.detailsText}><Text style={styles.boldText}>Notes:</Text> {appointment.notes || 'No additional notes'}</Text>
      </View>
      <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backButton}>
        <Text style={styles.backButtonText}>Back to Appointments</Text>
      </TouchableOpacity>
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
 
  const { appointment } = route.params;

  const [selectedDate, setSelectedDate] = useState('');
  const [selectedTime, setSelectedTime] = useState('');
  const availableTimeSlots = [
    "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM",
  ];

  const handleConfirm = () => {
    if (selectedDate && selectedTime) {
      Alert.alert(`Appointment Rebooked on ${selectedDate} at ${selectedTime}`);
      navigation.navigate('Home'); // Go back to the home screen after rebooking
    } else {
      Alert.alert('Please select both a date and a time slot.');
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.rebookContainer}>
      <Text style={styles.title}>Rebook Appointment</Text>
      <Text style={styles.text}>Appointment ID: {appointment.id}</Text>
      <Text style={styles.text}>Doctor: {appointment.doctor?.name}</Text>

      <Text style={styles.label}>Select Date:</Text>
      <Calendar
        onDayPress={day => setSelectedDate(day.dateString)}
        markedDates={{
          [selectedDate]: { selected: true, marked: true },
        }}
      />

      <Text style={styles.label}>Available Time Slots:</Text>
      <View style={styles.timeSlotsContainer}>
        {availableTimeSlots.map((slot) => (
          <TouchableOpacity
            key={slot}
            style={[styles.timeSlotButton, selectedTime === slot && styles.selectedTimeSlot]}
            onPress={() => setSelectedTime(slot)}
          >
            <Text style={styles.timeSlotText}>{slot}</Text>
          </TouchableOpacity>
        ))}
      </View>

      <TouchableOpacity onPress={handleConfirm} style={styles.confirmButton}>
        <Text style={styles.confirmButtonText}>Confirm Appointment</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backButton}>
        <Text style={styles.backButtonText}>Back</Text>
      </TouchableOpacity>
    </ScrollView>
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
        <TouchableOpacity 
          onPress={() => setSelectedTab('Complete')} 
          style={[styles.viewappointment_tabButton, selectedTab === 'Complete' && styles.viewappointment_tabButtonActive]}
        >
          <Text style={styles.viewappointment_tabText}>Complete</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          onPress={() => setSelectedTab('Upcoming')} 
          style={[styles.viewappointment_tabButton, selectedTab === 'Upcoming' && styles.viewappointment_tabButtonActive]}
        >
          <Text style={styles.viewappointment_tabText}>Upcoming</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          onPress={() => setSelectedTab('Cancelled')} 
          style={[styles.viewappointment_tabButton, selectedTab === 'Cancelled' && styles.viewappointment_tabButtonActive]}
        >
          <Text style={styles.viewappointment_tabText}>Cancelled</Text>
        </TouchableOpacity>
      </View>

      {/* Appointment List */}
      <ScrollView contentContainerStyle={styles.viewappointment_scrollContainer}>
        {filteredAppointments.map((appointment) => (
          <View key={appointment.id} style={styles.viewappointment_cardContainer}>
            <View style={styles.viewappointment_doctorInfo}>
              <Text style={styles.viewappointment_doctorName}>{appointment.doctor.name}</Text>
              <Text style={styles.viewappointment_specialty}>{appointment.doctor.specialty}</Text>
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
                  onPress={() => navigation.navigate('Rebook', { appointment })}
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
};

// Medical Records Screen


const MedicalRecordsScreen = () => {
  const [expandedVisitIndex, setExpandedVisitIndex] = useState(null);
  const [expandedPrescriptionIndex, setExpandedPrescriptionIndex] = useState(null); // Use a single index

  const toggleVisitExpand = (index) => {
    setExpandedVisitIndex(expandedVisitIndex === index ? null : index);
  };

  const togglePrescriptionExpand = (prescIndex) => {
    // Toggle the expansion of the prescription item
    setExpandedPrescriptionIndex(expandedPrescriptionIndex === prescIndex ? null : prescIndex);
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

      {/* Medical Conditions */}
      <View style={styles.rec_section}>
        <Text style={styles.rec_sectionHeader}>Medical Conditions</Text>
        {medicalRecord.medicalConditions.map((condition, conditionIndex) => (
          <View key={conditionIndex} style={styles.rec_conditionContainer}>
            <TouchableOpacity onPress={() => toggleVisitExpand(conditionIndex)}>
              <Text style={styles.rec_conditionName}>{condition.medCondition}</Text>
            </TouchableOpacity>
            {expandedVisitIndex === conditionIndex && (
              <View style={styles.rec_conditionDetails}>
                <Text style={styles.rec_infoText}>Notes: {condition.notes}</Text>
              </View>
            )}
          </View>
        ))}
      </View>

      {/* Medical Tests */}
      <View style={styles.rec_section}>
        <Text style={styles.rec_sectionHeader}>Medical Tests</Text>
        {medicalRecord.medicalTests.map((test, testIndex) => (
          <View key={testIndex} style={styles.rec_testContainer}>
            <TouchableOpacity onPress={() => toggleVisitExpand(testIndex)}>
              <Text style={styles.rec_testType}>{test.testType}</Text>
              <Text style={styles.rec_testSubject}>{test.subjectOfTest}</Text>
            </TouchableOpacity>
            {expandedVisitIndex === testIndex && (
              <View style={styles.rec_testDetails}>
                <Text style={styles.rec_infoText}>Result: {test.result}</Text>
                <Text style={styles.rec_infoText}>Uploaded on: {test.dateTimeOfUpload}</Text>
                <Image source={require('./assets/download1.png')} style={styles.rec_testImage} />
              </View>
            )}
          </View>
        ))}
      </View>

      {/* Prescriptions */}
      <View style={styles.rec_section}>
        <Text style={styles.rec_sectionHeader}>Prescriptions</Text>
        {medicalRecord.prescriptions.map((prescription, prescIndex) => (
          <View key={prescIndex} style={styles.rec_prescriptionContainer}>
            <TouchableOpacity onPress={() => togglePrescriptionExpand(prescIndex)}>
              <Text style={styles.rec_doctorName}>Doctor: {prescription.doctorName}</Text>
              <Text style={styles.rec_prescriptionDate}>Date: {prescription.dateOfPrescription}</Text>
            </TouchableOpacity>
            {expandedPrescriptionIndex === prescIndex && (
              <View style={styles.rec_prescriptionDetails}>
                {prescription.medicines.map((medicine, medicineIndex) => (
                  <View key={medicineIndex}>
                    <Text style={styles.rec_medicineName}>{medicine.medicineName}</Text>
                    <Text style={styles.rec_infoText}>Form of Intake: {medicine.formOfIntake}</Text>
                    <Text style={styles.rec_infoText}>Subscription Heading: {medicine.subscriptionHeading}</Text>
                    <Text style={styles.rec_infoText}>Duration of Intake: {medicine.durationOfIntake} days</Text>
                    <Text style={styles.rec_infoText}>Frequency of Intake: {medicine.frequencyOfIntake}</Text>
                    <Text style={styles.rec_infoText}>Side Effects: {medicine.sideEffects}</Text>
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
  recContainer: {
    padding: 20,
    backgroundColor: '#f9f9f9',
    fontFamily: 'Arial', 
  },
  recHeader: {
    padding: 20,
    textAlign: 'center',
    backgroundColor: '#4a90e2',
    borderRadius: 10,
    marginBottom: 20,
  },
  recHeaderText: {
    color: '#ffffff',
    fontSize: 24,
    fontWeight: 'bold',
  },
  recSection: {
    marginBottom: 20,
    backgroundColor: '#ffffff',
    padding: 15,
    borderRadius: 8,
    shadowColor: '#000000',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 1 },
    shadowRadius: 3,
  },
  recSectionHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333333',
    marginBottom: 10,
  },
  recInfoText: {
    fontSize: 16,
    color: '#666666',
    marginVertical: 5,
  },
  recVisitContainer: {
    marginBottom: 15,
  },
  recVisitButton: {
    width: '100%',
    padding: 10,
    textAlign: 'left',
    backgroundColor: '#e8f0fe',
    borderRadius: 5,
    borderWidth: 0,
    cursor: 'pointer', // React Native doesn't support cursor, so this can be omitted.
  },
  recVisitDate: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1a73e8',
  },
  recDoctorName: {
    fontSize: 16,
    color: '#555555',
  },
  recVisitDetails: {
    marginLeft: 15,
    marginTop: 10,
  },
  recPrescriptionContainer: {
    marginTop: 10,
  },
  recPrescriptionButton: {
    width: '100%',
    padding: 5,
    textAlign: 'left',
    backgroundColor: '#f0f4ff',
    borderRadius: 5,
    borderWidth: 0,
    cursor: 'pointer', // Same note as above
  },
  recMedicineName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1a73e8',
  },
  recPrescriptionDetails: {
    marginLeft: 15,
    marginTop: 10,
  },
  recSectionSubheader: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333333',
    marginTop: 10,
  },
  // Specific Styling
  recConditionContainer: {
    marginBottom: 10,
  },
  recTestContainer: {
    marginBottom: 10,
  },
  recPrescriptionContainer: {
    marginBottom: 10,
  },
  recConditionButton: {
    width: '100%',
    padding: 10,
    backgroundColor: '#007bff',
    color: 'white',
    borderWidth: 0,
    borderRadius: 4,
    cursor: 'pointer', // React Native doesn't support cursor
    textAlign: 'left',
  },
  recConditionButtonHover: {
    backgroundColor: '#0056b3',
  },
  recConditionName: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  recTestType: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  recDoctorName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#555555',
  },
  recConditionDetails: {
    padding: 10,
    backgroundColor: '#f9f9f9',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    marginTop: 10,
  },
  recTestDetails: {
    padding: 10,
    backgroundColor: '#f9f9f9',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    marginTop: 10,
  },
  recPrescriptionDetails: {
    padding: 10,
    backgroundColor: '#f9f9f9',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 4,
    marginTop: 10,
  },
  recTestImage: {
    width: '100%',
    height: 'auto',
    marginTop: 10,
  },
  detailsContainer: {
    padding: 30,
    maxWidth: 800,
    margin: '0 auto',
    backgroundColor: '#f9f9f9',
    borderRadius: 8,
  },
  headerText: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#333',
  },
  detailsContent: {
    marginBottom: 20,
    lineHeight: 1.8,
  },
  detailsText: {
    fontSize: 16,
    marginBottom: 10,
  },
  boldText: {
    fontWeight: 'bold',
  },
  backButton: {
    padding: 10,
    backgroundColor: '#007bff',
    borderRadius: 5,
    marginTop: 20,
  },
  backButtonText: {
    color: '#fff',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  cancelButton: {
    marginTop: 20,
    padding: 10,
    backgroundColor: '#f44336',
    borderRadius: 5,
  },
  cancelButtonText: {
    color: '#fff',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  rebookContainer: {
    padding: 16,
  },
  label: {
    marginTop: 20,
    fontSize: 16,
  },
  datePicker: {
    marginTop: 10,
    padding: 10,
    width: '100%',
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
  },
  timeSlotsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: 10,
  },
  timeSlotButton: {
    padding: 10,
    margin: 5,
    backgroundColor: '#007bff',
    borderRadius: 5,
  },
  selectedTimeSlot: {
    backgroundColor: '#4CAF50',
  },
  timeSlotText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  confirmButton: {
    backgroundColor: '#4CAF50',
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
    marginBottom: 20,
  },
  confirmButtonText: {
    fontSize: 18,
    color: '#fff',
    fontWeight: 'bold',
  },
  backButton: {
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
    backgroundColor: '#ccc',
  },
  backButtonText: {
    fontSize: 18,
    color: '#333',
  },
});

// Home Screen Styles
const homeStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    paddingTop: 50,
  },
  welcomeText: {
 fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
    paddingBottom: 20,
    borderBottomWidth: 2,
    borderBottomColor: '#BFDCF0',
    marginBottom: 30,
    width: '60%',
  color:'#616161', 
  },



  upperSection: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '60%',
    paddingBottom: 20,
    borderBottomWidth: 2,
    borderBottomColor: '#BFDCF0',
    marginBottom: 30,
  },
  /* Rectangle 1173 */



  profileIconContainer: {
    backgroundColor: '#E0E0E0',
    borderRadius: 50,
    padding: 20,
  },
  profileIcon: {
    width: 40,
    height: 40,
  },
  upperButtonsColumn: {
    flex: 1,
    marginLeft: 20,
    justifyContent: 'space-between',
  },
  widgetButton: {
    backgroundColor: '#E3F2FD',
    paddingVertical: 20,
    paddingHorizontal: 20,
    borderRadius: 20,
    marginBottom: 10,
    alignItems: 'center',
  },
  widgetText: {
    color: '#0D47A1',
    fontSize: 14,
  },
  lowerSection: {
    width: '90%',
    marginTop: 20,
  },
  lowerButtonsRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 20,
  },

  lowerWidgetButton: {
    backgroundColor: '#E3F2FD',
    
    paddingVertical: 20,
    paddingHorizontal: 15,
    borderRadius: 10,
    width: '45%',
    alignItems: 'center',
  },
  lowerWidgetText: {
    color: '#0D47A1',
    fontSize: 14,
    textAlign: 'top',
  },
  infoWidgetButton: {
    backgroundColor: '#BBDEFB',
    paddingBottom: 80,
    paddingHorizontal: 10,
    borderBottomColor: '#BFDCF0',
    borderRadius: 10,
    width: '45%',
    alignItems: 'flex-center', 
    justifyContent: 'flex-top',  // Positions children at the top
  },
  infoWidgetText: {
    backgroundColor: '#0D47A1',
    color: 'white',
    fontSize: 14,
    fontWeight: 'bold',
    textAlignVertical: 'top',  // For Android: aligns text to the top vertically
    textAlign: 'center',         // Aligns text horizontally to the left
  },
  infoWidget: {
    backgroundColor: '#fff',
    padding: 10,
    borderRadius: 5,
    marginBottom: 10,
    elevation: 2,
  },
  subtitle: {
    fontSize: 14,
    color: '#333',
  },
});


