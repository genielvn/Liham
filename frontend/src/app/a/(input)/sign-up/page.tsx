"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import style from "./page.module.scss";
import { getUniversities, signUpUser } from "@/services/api";

export default function AccountSignUp() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [email, setEmail] = useState("");
    const [university, setUniversity] = useState("");
    const [universities, setUniversities] = useState([]);
    const [errorMessage, setErrorMessage] = useState("");
    const router = useRouter();

    useEffect(() => {
        const fetchUniversities = async () => {
            try {
                const response = await getUniversities();
                setUniversities(response.data);
            } catch (error) {
                console.error("Error fetching universities:", error);
            }
        };
        fetchUniversities();
    }, [router]);

    const handleSignUpSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setErrorMessage("");

        if (password !== confirmPassword) {
            setErrorMessage("Passwords do not match!");
            return;
        }

        try {
            const response = await signUpUser(
                username,
                password,
                email,
                university
            );
            router.push("/f");
        } catch (error: any) {
            setErrorMessage(
                error.response?.data?.error ||
                    "Something went wrong. Please try again."
            );
        }
    };

    return (
        <>
            <h1> Welcome!</h1>
            <form onSubmit={handleSignUpSubmit}>
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
                <div className={style.account__input_divider}>
                    <label htmlFor="confirm-password">Confirm Password</label>
                    <input
                        type="password"
                        id="confirm-password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        required
                    />
                </div>
                <div className={style.account__input_divider}>
                    <label htmlFor="email">School Email</label>
                    <input
                        type="text"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className={style.account__input_divider}>
                    <label htmlFor="university">Select University</label>
                    <select
                        id="university"
                        value={university}
                        onChange={(e) => setUniversity(e.target.value)}
                        required
                    >
                        <option value="" disabled>
                            Choose your university
                        </option>
                        {universities.map(
                            (uni: { university_id: string; name: string }) => (
                                <option
                                    key={uni.university_id}
                                    value={uni.university_id}
                                >
                                    {uni.name}
                                </option>
                            )
                        )}
                    </select>
                </div>
                {errorMessage && (
                    <p className={style.account__input_divider}>
                        {errorMessage}
                    </p>
                )}
                <div className={style.account__input_buttons}>
                    <button
                        type="button"
                        className="btn-full-width btn-hollow-pink margin-bottom-20"
                        onClick={() => router.push("/a/sign-in")}
                    >
                        {"Already have an account?"}
                    </button>
                    <button
                        type="submit"
                        className="btn-full-width btn-solid-pink"
                    >
                        Sign Up
                    </button>
                </div>
            </form>
        </>
    );
}
