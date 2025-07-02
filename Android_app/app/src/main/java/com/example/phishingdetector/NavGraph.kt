package com.example.phishingdetector

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable

@Composable
fun NavGraph(navController: NavHostController){
    NavHost(navController=navController, startDestination="home_screen"){
        composable("home_screen"){
            Homescreen(onNavigate = {prediction ->
                navController.navigate("result_screen/$prediction")
            })
        }
        composable("result_screen/{prediction}") { backStackEntry ->
            val prediction = backStackEntry.arguments?.getString("prediction") ?: "Unknown"
            Resultscreen(
                prediction = prediction,
                onBack = { navController.popBackStack() }
            )
        }
    }
}