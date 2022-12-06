#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


int main() {
    std::ifstream in("in.txt");
    if (!in) {
        std::cout << "Error opening file" << "\n";
        return 1;
    }

    std::string line;
    std::vector<int> calorie_list { 0 };

    int i = 0;
    while(getline(in, line)) {
        if (line == "") {
            calorie_list.push_back(0);
            i++;
        }
        else {
            calorie_list[i] += stoi(line);
        }
    }

    int max = 0;
    for (int i = 0; i < calorie_list.size(); i++) {
        if (calorie_list[i] > max) {
            max = calorie_list[i];
        }
    }

    // sort the list
    sort(calorie_list.begin(), calorie_list.end());

    int size = calorie_list.size();
    std::cout << "Max: " << calorie_list[size -1] << "\n";
    std::cout << "Top Three: " << (calorie_list[size-1] + calorie_list[size-2] + calorie_list[size-3]) << "\n";
}