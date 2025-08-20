class CarNode:
    """
    Node to represent each parked car in the linked list.
    """
    def __init__(self, license_plate, slot_number):
        self.license_plate = license_plate
        self.slot_number = slot_number
        self.next = None


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity  # Simulate dynamic memory allocation of slots
        self.head = None  # Head of linked list
        self.tail = None
        self.active_cars = 0

    def is_full(self):
        return self.active_cars == self.capacity

    def is_empty(self):
        return self.active_cars == 0

    def allocate_slot(self):
        for i in range(self.capacity):
            if self.slots[i] is None:
                return i
        return -1  # No free slot found

    def park_car(self, license_plate):
        if self.is_full():
            print(f"Parking Full: Cannot park car {license_plate}")
            return

        slot = self.allocate_slot()
        if slot == -1:
            print(f"Error: Could not find available slot for {license_plate}")
            return

        # Mark slot as occupied
        self.slots[slot] = license_plate
        new_car = CarNode(license_plate, slot)

        # Add to linked list
        if not self.head:
            self.head = self.tail = new_car
        else:
            self.tail.next = new_car
            self.tail = new_car

        self.active_cars += 1
        print(f"Car {license_plate} parked at slot {slot}")

    def exit_car(self, license_plate):
        if self.is_empty():
            print("Parking lot is empty.")
            return

        prev = None
        current = self.head

        while current:
            if current.license_plate == license_plate:
                # Free the slot
                self.slots[current.slot_number] = None
                print(f"Car {license_plate} exited from slot {current.slot_number}")

                # Remove from linked list
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current == self.tail:
                    self.tail = prev

                self.active_cars -= 1
                return
            prev = current
            current = current.next

        print(f"Car {license_plate} not found in the lot.")

    def display_parked_cars(self):
        if self.is_empty():
            print("No cars parked.")
            return

        print("Currently parked cars:")
        current = self.head
        while current:
            print(f" - Car {current.license_plate} at slot {current.slot_number}")
            current = current.next


# Example Usage
if __name__ == "__main__":
    lot = ParkingLot(capacity=3)

    lot.park_car("KA01AB1234")
    lot.park_car("MH02CD5678")
    lot.park_car("DL03EF9012")

    lot.display_parked_cars()

    # Attempting overflow
    lot.park_car("GJ04GH3456")

    # Exiting a car
    lot.exit_car("MH02CD5678")
    lot.display_parked_cars()

    # Parking again after a car has left
    lot.park_car("GJ04GH3456")
    lot.display_parked_cars()
