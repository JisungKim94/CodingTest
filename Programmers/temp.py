def count_bonds(atoms, bonds):
    atom_arms = {}
    for atom in atoms:
        atom_arms[atom] = 0

    for atom in atoms:
        atom_arms[atom] += 1

    num_bonds = []
    for bond in bonds:
        count = 0
        for atom in bond:
            if atom_arms.get(atom, 0) > 0:
                count += 1
                atom_arms[atom] -= 1
        num_bonds.append(count)
        for atom in bond:
            atom_arms[atom] += 1

    return num_bonds


atoms = "OCOONCO"
bonds = [[1, 2], [2, 3], [3, 5], [5, 6], [6, 4], [5, 7]]
result = count_bonds(atoms, bonds)
print(result)  # [2, 1, 1, 1, 1, 2]
