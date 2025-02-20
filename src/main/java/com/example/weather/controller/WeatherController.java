package com.example.weather.controller;

import com.example.weather.model.WeatherPrediction;
import com.example.weather.service.WeatherService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Controller
public class WeatherController {

    @Autowired
    private WeatherService weatherService;

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @PostMapping("/predict")
    public String predict(
            @RequestParam("startDate") String startDate,
            @RequestParam("endDate") String endDate,
            Model model) {

        // Parse the input dates
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate start = LocalDate.parse(startDate, formatter);
        LocalDate end = LocalDate.parse(endDate, formatter);

        // Call the service to get predictions
        List<WeatherPrediction> predictions = weatherService.predictWeather(start, end);

        // Add predictions to the model
        model.addAttribute("predictions", predictions);

        return "index";
    }
}