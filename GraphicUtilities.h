#ifndef GRAPHICUTILITIES_H
#define GRAPHICUTILITIES_H

#include <vector>
#include <string>
#include <iostream>

class ProgressBar
{
public:
    /**
     * @brief Construct a new Progress Bar object
     * 
     */
    ProgressBar();

    /**
     * @brief Destroy the Progress Bar object
     * 
     */
    ~ProgressBar();

    /**
     * @brief Make a new percent bar
     * 
     * @param prefix 
     */
    void newPercentBar(int bar_width=60, std::string prefix="");

    /**
     * @brief Display a percent bar
     * 
     * @param index 
     */
    void displayPercentBar(int index=0);

    void updatePercentBar(float val, int index=0);

    void deletePercentBar(int index=0);

private:
    struct PercentBar
    {
        int         bar_width;
        float       progress;
        std::string prefix;
        std::string text;
    };

    std::vector<PercentBar> mPercentBars;
};

#endif //GRAPHICUTILITIES_H