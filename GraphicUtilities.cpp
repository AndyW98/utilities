#include "GraphicUtilities.h"

ProgressBar::ProgressBar(){}

ProgressBar::~ProgressBar()
{
    for (int i = 0; i < mPercentBars.size(); i++)
    {
        deletePercentBar(i);
    }
}

void ProgressBar::newPercentBar(int bar_width, std::string prefix)
{
    PercentBar new_percent_bar = {
        .bar_width  = bar_width,
        .progress   = 0.0,
        .prefix     = prefix,
        .text       = ""
    };
    mPercentBars.push_back(new_percent_bar);
    displayPercentBar();
}

void ProgressBar::displayPercentBar(int index)
{
    if (mPercentBars.size() <= 0)
        return;
    
    PercentBar bar = mPercentBars[index];

    std::string updated_text = bar.prefix + "[";

    int pos = bar.bar_width * bar.progress;
    for (int i = 0; i < bar.bar_width; ++i)
    {
        if (i < pos)
            updated_text += '=';
        else if (i == pos)
            updated_text += '>';
        else
            updated_text += ' ';
    }
    updated_text += ("] " + std::to_string(int(bar.progress * 100.0)) + " %\r");
    mPercentBars[index].text = updated_text;
    std::cout << updated_text;
    std::cout.flush();
}

void ProgressBar::updatePercentBar(float val, int index)
{
    mPercentBars[index].progress = val;
    displayPercentBar(index);
}

void ProgressBar::deletePercentBar(int index)
{
    std::cout << "\n";
    std::cout.flush();
}