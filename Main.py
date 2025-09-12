# Fiber Optic Link Budget Calculator
# Author: Med Amine
# Description: Simple Python tool to calculate total link loss and margin

def calculate_link_budget(length_km, fiber_loss_db_km, splice_loss_db, num_splices,
                          connector_loss_db, num_connectors,
                          transmitter_power_dbm, receiver_sensitivity_dbm):
    """
    Calculate fiber optic link budget
    """

    # Fiber attenuation
    fiber_loss = length_km * fiber_loss_db_km

    # Total splice loss
    total_splice_loss = num_splices * splice_loss_db

    # Total connector loss
    total_connector_loss = num_connectors * connector_loss_db

    # Total link loss
    total_loss = fiber_loss + total_splice_loss + total_connector_loss

    # Power margin. 
    received_power = transmitter_power_dbm - total_loss
    margin = received_power - receiver_sensitivity_dbm

    return total_loss, received_power, margin


if __name__ == "__main__":
    print("📡 Fiber Optic Link Budget Calculator 📡")

    # Example input values (you can later change to user input)
    length_km = float(input("Enter fiber length (km): "))
    fiber_loss_db_km = float(input("Enter fiber loss (dB/km): "))
    splice_loss_db = float(input("Enter splice loss (dB per splice): "))
    num_splices = int(input("Enter number of splices: "))
    connector_loss_db = float(input("Enter connector loss (dB per connector): "))
    num_connectors = int(input("Enter number of connectors: "))
    transmitter_power_dbm = float(input("Enter transmitter power (dBm): "))
    receiver_sensitivity_dbm = float(input("Enter receiver sensitivity (dBm): "))

    total_loss, received_power, margin = calculate_link_budget(
        length_km, fiber_loss_db_km,
        splice_loss_db, num_splices,
        connector_loss_db, num_connectors,
        transmitter_power_dbm, receiver_sensitivity_dbm
    )

    print("\n📊 Results:")
    print(f"➡️ Total Link Loss: {total_loss:.2f} dB")
    print(f"➡️ Received Power: {received_power:.2f} dBm")
    print(f"➡️ Power Margin: {margin:.2f} dB")
