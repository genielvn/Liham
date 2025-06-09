"use client";

import ThreadReplyTab from "@/components/ThreadReplyTab";
import UserBanner from "@/components/UserBanner";
import { notFound } from "next/navigation";
import { UserBoardThreadData } from "@/types/userboardthread";
import { useEffect, useState } from "react";
import { getSelfUserData } from "@/services/api";

export default function UserYou() {
    const [data, setData] = useState<UserBoardThreadData | null>(null);
    const [error, setError] = useState(false);

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await getSelfUserData();
                setData(response.data);
            } catch (error) {
                setError(true);
            }
        };
        fetchUserData();
    }, []);

    if (error) {
        return notFound();
    }

    return (
        data && (
            <>
                <UserBanner data={data?.user} />
                <ThreadReplyTab data={data} />
            </>
        )
    );
}
