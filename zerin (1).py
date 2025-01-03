import numpy as np
from abc import ABC, abstractmethod

# Abstract base class for Hospital
class AbstractHospital(ABC):
    @abstractmethod
    def add_patient(self, patient):
        pass

    @abstractmethod
    def add_doctor(self, doctor):
        pass

    @abstractmethod
    def get_patients(self):
        pass

    @abstractmethod
    def get_doctors(self):
        pass


# Implementing the abstract class
class Hospital(AbstractHospital):
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def get_patients(self):
        return [patient.get_patient_details() for patient in self.patients]

    def get_doctors(self):
        return [doctor.get_doctor_details() for doctor in self.doctors]


# Base class for Person using Encapsulation
class Person:
    def __init__(self, name, age, gender):
        self._name = name.strip().title()
        self._age = age
        self._gender = gender.strip().capitalize()

    def get_details(self):
        return {
            "Name": self._name,
            "Age": self._age,
            "Gender": self._gender
        }


# Inherited Class for Patients
class Patient(Person):
    def __init__(self, name, age, gender, patient_id, ailment):
        super().__init__(name, age, gender)
        self.patient_id = patient_id.strip()
        self.ailment = ailment.strip().capitalize()

    def get_patient_details(self):
        details = self.get_details()
        details.update({
            "Patient ID": self.patient_id,
            "Ailment": self.ailment
        })
        return details


# Inherited Class for Doctors
class Doctor(Person):
    def __init__(self, name, age, gender, doctor_id, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id.strip()
        self.specialization = specialization.strip().capitalize()

    def get_doctor_details(self):
        details = self.get_details()
        details.update({
            "Doctor ID": self.doctor_id,
            "Specialization": self.specialization
        })
        return details


# Utility Functions
def find_by_id(collection, _id, id_type):
    for item in collection:
        if (id_type == "patient" and item.patient_id == _id) or (id_type == "doctor" and item.doctor_id == _id):
            return item
    return None


def search_patient_by_id(hospital, patient_id):
    patient = find_by_id(hospital.patients, patient_id.strip(), "patient")
    if patient:
        return patient.get_patient_details()
    else:
        return "Patient not found!"


def search_doctor_by_id(hospital, doctor_id):
    doctor = find_by_id(hospital.doctors, doctor_id.strip(), "doctor")
    if doctor:
        return doctor.get_doctor_details()
    else:
        return "Doctor not found!"


def print_heading_with_underline(heading):
    print(heading)
    print("=" * len(heading))


# Main Interaction Function
def main():
    hospital = Hospital()
    ailments_set = set()
    specializations_dict = {}

    while True:
        print("\nWelcome to the Enhanced Hospital Management System")
        print("1. Add a Patient")
        print("2. Add a Doctor")
        print("3. View All Patients")
        print("4. View All Doctors")
        print("5. Search Patient by ID")
        print("6. Search Doctor by ID")
        print("7. View Age Statistics")
        print("8. List Unique Ailments")
        print("9. List Doctors by Specialization")
        print("10. Sort Patients by Age")
        print("11. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                name = input("Enter Patient's Name: ").strip().title()
                age = int(input("Enter Patient's Age: "))
                gender = input("Enter Patient's Gender (Male/Female): ").strip().capitalize()
                patient_id = input("Enter Patient ID: ").strip()
                ailment = input("Enter Patient's Ailment: ").strip().capitalize()
                hospital.add_patient(Patient(name, age, gender, patient_id, ailment))
                ailments_set.add(ailment)
                print("Patient added successfully!")
            except ValueError:
                print("Error: Invalid input for age. Please try again.")

        elif choice == 2:
            try:
                name = input("Enter Doctor's Name: ").strip().title()
                age = int(input("Enter Doctor's Age: "))
                gender = input("Enter Doctor's Gender (Male/Female): ").strip().capitalize()
                doctor_id = input("Enter Doctor ID: ").strip()
                specialization = input("Enter Doctor's Specialization: ").strip().capitalize()
                hospital.add_doctor(Doctor(name, age, gender, doctor_id, specialization))
                specializations_dict.setdefault(specialization, []).append(name)
                print("Doctor added successfully!")
            except ValueError:
                print("Error: Invalid input for age. Please try again.")

        elif choice == 3:
            print_heading_with_underline("All Patients:")
            for patient in hospital.get_patients():
                print(patient)

        elif choice == 4:
            print_heading_with_underline("All Doctors:")
            for doctor in hospital.get_doctors():
                print(doctor)

        elif choice == 5:
            patient_id = input("Enter Patient ID to search: ").strip()
            print(search_patient_by_id(hospital, patient_id))

        elif choice == 6:
            doctor_id = input("Enter Doctor ID to search: ").strip()
            print(search_doctor_by_id(hospital, doctor_id))

        elif choice == 7:
            ages = [person.get_details()["Age"] for person in hospital.patients + hospital.doctors]
            if ages:
                age_array = np.array(ages)
                print_heading_with_underline("Age Statistics:")
                print("Average Age:", np.mean(age_array))
                print("Maximum Age:", np.max(age_array))
                print("Minimum Age:", np.min(age_array))
            else:
                print("No data available for statistics.")

        elif choice == 8:
            print_heading_with_underline("Unique Ailments:")
            print(ailments_set)

        elif choice == 9:
            print_heading_with_underline("Doctors by Specialization:")
            for specialization, doctors in specializations_dict.items():
                print(f"{specialization}: {', '.join(doctors)}")

        elif choice == 10:
            sorted_patients = sorted(hospital.get_patients(), key=lambda patient: patient['Age'])
            print_heading_with_underline("Sorted Patients by Age:")
            for patient in sorted_patients:
                print(patient)

        elif choice == 11:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the interactive system
if __name__ == "__main__":
    main()
