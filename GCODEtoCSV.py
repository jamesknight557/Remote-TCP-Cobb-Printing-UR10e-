import csv

def gcode_to_csv(gcode_path, csv_path, tool_orientation=(0, 0, 0)):
    current_pos = {'X': 0.0, 'Y': 0.0, 'Z': 0.0}
    curve_written = False  # Track if 'Curve' has been written
    z_offset = 0.0
    last_layer = None

    with open(gcode_path, 'r') as gcode_file, open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        row_count = 0
        for line in gcode_file:
            line = line.strip()
            # Detect new layer
            if line.startswith(';LAYER:'):
                try:
                    layer_num = int(line.split(':')[1])
                    if last_layer is not None and layer_num != last_layer:
                        z_offset += 5.0
                    last_layer = layer_num
                except Exception:
                    continue

            if line.startswith('G1'):  # Only G1 motion commands
                # Extract X, Y, Z if present
                for axis in ['X', 'Y', 'Z']:
                    if axis in line:
                        try:
                            val = float(line.split(axis)[1].split()[0])
                            current_pos[axis] = val
                        except Exception:
                            continue
                row_count += 1
                z_value = current_pos['Z'] + z_offset
                if row_count == 1 and not curve_written:
                    writer.writerow([
                        current_pos['X'], current_pos['Y'], z_value,
                        *tool_orientation, 'Curve'
                    ])
                    curve_written = True
                else:
                    writer.writerow([
                        current_pos['X'], current_pos['Y'], z_value,
                        *tool_orientation
                    ])

# Example usage:
gcode_to_csv('10mm.gcode', '10mm.csv', tool_orientation=(0, 0, -1))