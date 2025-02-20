package com.example.weather.service;

import com.example.weather.model.WeatherPrediction;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

@Service
public class WeatherService {

    public List<WeatherPrediction> predictWeather(LocalDate startDate, LocalDate endDate) {
        List<WeatherPrediction> predictions = new ArrayList<>();
        long numDays = ChronoUnit.DAYS.between(startDate, endDate) + 1;

        for (int i = 0; i < numDays; i++) {
            LocalDate currentDate = startDate.plusDays(i);
            int dayOfYear = currentDate.getDayOfYear();
            int month = currentDate.getMonthValue();

            try {
                // Call the Python script
                ProcessBuilder pb = new ProcessBuilder(
                        "python",
                        "src/main/resources/predict.py",
                        String.valueOf(dayOfYear),
                        String.valueOf(month)
                );
                Process process = pb.start();

                // Read the output
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line = reader.readLine();

                // Parse the output (comma-separated values)
                String[] values = line.split(",");
                double temperature = Double.parseDouble(values[0]);
                double humidity = Double.parseDouble(values[1]);
                double windSpeed = Double.parseDouble(values[2]);
                double pressure = Double.parseDouble(values[3]);

                // Create a WeatherPrediction object
                predictions.add(new WeatherPrediction(currentDate, temperature, humidity, windSpeed, pressure));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        return predictions;
    }
}