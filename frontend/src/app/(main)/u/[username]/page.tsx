"use client";

import ThreadReplyTab from "@/components/ThreadReplyTab";
import UserBanner from "@/components/UserBanner";
import { notFound } from "next/navigation";
import { UserBoardThreadData } from "@/types/userboardthread";
import { banUser, getSelfUserData, getUserData } from "@/services/api";
import { useEffect, useState } from "react";

interface UserProps {
    params: { username: string };
}

export default function UserOthers({ params }: UserProps) {
    const { username } = params;

    const [data, setData] = useState<UserBoardThreadData | null>(null);
    const [isAdmin, setIsAdmin] = useState(false);
    const [error, setError] = useState(false);

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await getUserData(username);
                setData(response.data);
            } catch (error) {
                setError(true);
            }
        };
        const fetchAdmin = async () => {
            try {
                const response = await getSelfUserData();
                setIsAdmin(response.data.user.is_admin);
            } catch (error) {
                console.error("Error fetching user data:", error);
            }
        };
        fetchAdmin();
        fetchUserData();
    }, []);

    const handleBanUser = async () => {
        try {
            const response = await banUser(username);
            alert("Toggle ban successfully done");
            window.location.reload();
        } catch (error) {
            console.error("Error banning user:", error);
            alert("An error has occured.");
        }
    };

    if (error) {
        return notFound();
    }

    return (
        data && (
            <>
                <UserBanner data={data?.user} />
                <ThreadReplyTab data={data} />
                {isAdmin && (
                    <div className="margin-top-5">
                        <h2>Moderator Settings</h2>
                        <button
                            className="btn-small btn-red"
                            onClick={handleBanUser}
                        >
                            {data?.user.is_banned === true
                                ? "Unban User"
                                : "Ban User"}
                        </button>
                    </div>
                )}
            </>
        )
    );
}
