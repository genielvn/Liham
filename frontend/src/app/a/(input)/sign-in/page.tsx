"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import style from "./page.module.scss";
import { loginUser } from "@/services/api";

export default function AccountSignIn() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const router = useRouter();

    const handleSignInSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setErrorMessage("");
    
        try {
            const response = await loginUser(username, password);
            router.push("/f");
        } catch (error: any) {
            setErrorMessage(error.response?.data?.error || "Invalid credentials.");
        }
    };

    return (
        <>
            <h1> Welcome back! </h1>
            <form onSubmit={handleSignInSubmit}>
                <div className={style.account__input_divider}>
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className={style.account__input_divider}>
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                {errorMessage && (
                    <p className={style.error_message}>{errorMessage}</p>
                )}
                <div className={style.account__input_buttons}>
                    <button
                        type="button"
                        className="btn-full-width btn-hollow-pink margin-bottom-20"
                        onClick={() => router.push("/a/sign-up")}
                    >
                        {"Don't have an account?"}
                    </button>
                    <button
                        type="submit"
                        className="btn-full-width btn-solid-pink"
                    >
                        Sign In
                    </button>
                </div>
            </form>
        </>
    );
}
